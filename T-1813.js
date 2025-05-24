import { OpenAIToolSet } from "composio-core";
// 3k3bebb!vojhg7fp
// eoc1z2nm2ue!arm7  ---! inseretd


const toolset = new OpenAIToolSet();


// const res = await toolset.connectedAccounts.initiate({
//     entityId: "<entityId>",
//     authMode: "OAUTH2",
//     integrationId: "<integrationId>",
//     redirectUri: "<redirectUri>"
// })




const connection = await toolset.connectedAccounts.initiate({ 
    appName: "dropbox",
    integrationId: "e384d22b-873e-4c26-8527-a845f3735520", // or other app name
    entityId: "errorrep2noredurl",  // optional, identifies your end user
      // optional, alternative to appName
});
console.log(`Open this URL to authenticate: ${connection.redirectUrl}`);



// import { OpenAIToolSet } from "composio-core";
// const composioToolset = new OpenAIToolSet();

// const integration = await composioToolset.integrations.create({
//   appUniqueKey: "dropbox",
//   name: "Integrationdrop1",
//   authScheme: "OAUTH2",
//   useComposioAuth: true,
//   authConfig: {
//     client_id: "",
//     client_secret: "",
//     redirect_uri: "https://backend.composio.dev/api/v1/auth-apps/add"
//   },
// });


// const user_id = "testing2";
// const entity = await composioToolset.getEntity(user_id);

// const thread_id = "12345678"; 
// const redirect_url = `https://backend.composio.dev/api/v1/auth-apps/add/${thread_id}`; // Example redirect URL

// const connectionRequest = await entity.initiateConnection({
//   integrationId: "1732cd84-8239-45a3-824b-cdac58933c9b",
//   useComposioAuth: false,
//   redirectUri: redirect_url,
// });

// console.log(connectionRequest.redirectUrl);






// import { OpenAIToolSet } from "composio-core";

// const composioToolset = new OpenAIToolSet();

// const integration = await composioToolset.integrations.create({
//     name: "NewIntnotwhite",
//     appUniqueKey: "dropbox",
//     useComposioAuth: true,
//     forceNewIntegration: true,
// })

// console.log(integration.id)
