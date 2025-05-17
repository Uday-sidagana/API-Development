// import { Request, Response } from 'express';
// import OpenAI from 'openai';
// import { OpenAIToolSet } from '@composio/openai';

// interface User {
//   userId: string | number;
// }

// export const sharePost = async (req: Request, res: Response) => {
//   try {
//     async sharePost(req: Request, res: Response) {
//         try {
//             const { text, imageUrl, scheduleTime } = req.body;
//             const userId = (req.user as User)?.userId.toString() + "linkedin";

//             // Initialize OpenAI and Composio clients
//             const openaiClient = new OpenAI({ apiKey: process.env.OPENAI_API_KEY! });
//             const composioToolset = new OpenAIToolSet({ 
//                 apiKey: process.env.COMPOSIO_API_KEY!, 
//                 entityId: userId 
//             });

//             // Get the LinkedIn post creation tool
//             const tools = await composioToolset.getTools({ 
//                 actions: ["LINKEDIN_CREATE_LINKED_IN_POST"] 
//             });

//             // Create an instruction that includes the post content and image
//             const instruction = `Create a LinkedIn post with the following content: "${text}"${imageUrl ? ` and include the image from URL: "${imageUrl}"` : ''}`;

//             // Call the OpenAI model with the tool
//             const response = await openaiClient.chat.completions.create({
//                 model: "gpt-4-turbo",
//                 messages: [{ role: "user", content: instruction }],
//                 tools,
//                 tool_choice: "auto"
//             });

//             // Handle the tool call
//             const toolResponse = await composioToolset.handleToolCall(response);
//             const parsedResponse = toolResponse.map((item: any) =>
//                 typeof item === 'string' ? JSON.parse(item) : item
//             );

//             // If scheduleTime is provided, store it in the DB
//             if (scheduleTime) {
//                 const scheduleDate = new Date(scheduleTime);
//                 if (scheduleDate > new Date()) {
//                     // TODO: Implement scheduling logic here
//                     return res.status(200).json({ 
//                         success: true, 
//                         message: `Post scheduled for ${scheduleDate}`,
//                         data: parsedResponse 
//                     });
//                 }
//             }

//             return res.status(200).json({
//                 data: parsedResponse
//             });

//         } catch (err) {
//             console.error("LinkedIn post error:", err);
//             return res.status(500).json({ error: "Failed to share LinkedIn post" });
//         }
//     }
//     // ... your existing sharePost implementation ...
//   } catch (err) {
//     console.error("LinkedIn post error:", err);
//     return res.status(500).json({ error: "Failed to share LinkedIn post" });
//   }
// };