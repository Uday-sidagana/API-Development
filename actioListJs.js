// rxm0maku1xbgzk!s9q8j --------inserted ! and also this is abhishek's 

import fs from 'fs';

async function fetchAllToolsWithRetry(apiKey, baseUrl = 'https://backend.composio.dev', options = {}) {
    const {
      maxRetries = 3,
      retryDelay = 1000,
      requestDelay = 10 // delay between requests to avoid rate limiting
    } = options;
    
    const allTools = [];
    const longSlugTools = []; // Collect tools with long slugs
    let cursor = null;
    let hasMore = true;
    
    const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));
    
    async function makeRequest(url, attempt = 1) {
      try {
        const response = await fetch(url.toString(), {
          headers: {
            'x-api-key': apiKey
          }
        });
        
        if (!response.ok) {
          if (response.status === 429 && attempt <= maxRetries) {
            // Rate limited, wait and retry with exponential backoff
            console.log(`Rate limited, retrying in ${retryDelay * attempt}ms...`);
            await delay(retryDelay * attempt);
            return makeRequest(url, attempt + 1);
          }
          throw new Error(`HTTP error! status: ${response.status}, ${response.statusText}`);
        }
        
        return await response.json();
      } catch (error) {
        if (attempt <= maxRetries && error.name !== 'SyntaxError') {
          console.log(`Request failed (attempt ${attempt}), retrying in ${retryDelay * attempt}ms...`);
          await delay(retryDelay * attempt);
          return makeRequest(url, attempt + 1);
        }
        throw error;
      }
    }
    
    while (hasMore) {
      const url = new URL(`${baseUrl}/api/v3/tools`);
      
      if (cursor) {
        url.searchParams.append('cursor', cursor);
      }
      
      url.searchParams.append('limit', '1000');
      
      try {
        const data = await makeRequest(url);
        data.items.forEach(item => {
            if (item.slug.length > 64 && item.deprecated.is_deprecated === false) {
                console.log(item.slug);
                longSlugTools.push({
                    slug: item.slug,
                    name: item.name,
                    toolkit: item.toolkit.name,
                    description: item.description
                });
            }
        })
        allTools.push(...data.items);
        
        if (data.next_cursor) {
          cursor = data.next_cursor;
          // Add small delay between requests to be respectful to the API
          await delay(requestDelay);
        } else {
          hasMore = false;
        }
        
        console.log(`Fetched ${data.items.length} tools. Total: ${allTools.length}/${data.total_pages * 100} (estimated)`);
        
      } catch (error) {
        console.error('Error fetching tools:', error);
        throw error;
      }
    }
    
    return { allTools, longSlugTools };
  }
  
  // Usage with options
  const apiKey = '';
  fetchAllToolsWithRetry(apiKey, 'https://backend.composio.dev', {
    maxRetries: 5,
    retryDelay: 2000,
    requestDelay: 200
  })
    .then(({ allTools, longSlugTools }) => {
      console.log(`\n✅ Successfully fetched ${allTools.length} tools!`);
      
      // Group by toolkit for better overview
      const toolsByToolkit = allTools.reduce((acc, tool) => {
        const toolkit = tool.toolkit.name;
        if (!acc[toolkit]) acc[toolkit] = [];
        acc[toolkit].push(tool);
        return acc;
      }, {});
      
      console.log('\n📊 Tools by Toolkit:');
      Object.entries(toolsByToolkit).forEach(([toolkit, tools]) => {
        console.log(`  ${toolkit}: ${tools.length} tools`);
      });
      
      // Prepare output data
      const outputData = {
        summary: {
          totalTools: allTools.length,
          longSlugToolsCount: longSlugTools.length,
          toolsByToolkit: Object.entries(toolsByToolkit).map(([toolkit, tools]) => ({
            toolkit,
            count: tools.length
          }))
        },
        longSlugTools: longSlugTools,
        allTools: allTools
      };
      
      // Write to JSON file
      const outputFilename = `composio_tools_${new Date().toISOString().split('T')[0]}.json`;
      fs.writeFileSync(outputFilename, JSON.stringify(outputData, null, 2));
      console.log(`\n💾 Data written to ${outputFilename}`);
      console.log(`📋 Found ${longSlugTools.length} tools with slugs longer than 64 characters`);
      
      return allTools;
    })
    .catch(error => {
      console.error('❌ Failed to fetch all tools:', error);
    });
