// // Example: Create a GitHub Issue Directly
// import { OpenAIToolSet } from "composio-core";
// // Assumes toolset is initialized and authenticated

// const toolset = new OpenAIToolSet();

// async function createIssue() {
//   console.log("Creating GitHub issue directly...");
//   try {
//     const result = await toolset.executeAction({
//       action: "LINKEDIN_CREATE_LINKED_IN_POST", // Use Enum for type safety
//       params: {
//         author:"urn:li:person:s6v7d9qvl2",
//         commentary:"ComposioTest",
//       },
//       // entityId: "your-user-id" // Optional: Specify if not 'default'
//     });

//     if (result.successful) {
//       console.log("Successfully created issue!");
//       // Issue details are often in result.data
//       console.log("Issue URL:", (result.data as any)?.html_url);
//     } else {
//       console.error("Failed to create issue:", result.error);
//     }
//   } catch (error) {
//     console.error("An error occurred:", error);
//   }
// }

// createIssue();

