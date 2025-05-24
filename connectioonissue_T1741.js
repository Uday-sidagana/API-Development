import axios from 'axios';

async function createConnection(payload) {
    try {
        const { key, integrationId, name, additionalInfo = {}, entityId, authConfig } = payload;

        const url = 'https://backend.composio.dev/api/v2/connectedAccounts/initiateConnection';
        const headers = {
            "Content-Type": "application/json",
            "x-api-key": "" // <-- Replace with your real API key!
        };

        const requestPayload = {
            app: { uniqueKey: key.toLowerCase(), integrationId },
            config: { name, ...authConfig },
            connection: {
                initiateData: additionalInfo,
                entityId
            }
        };

        const response = await axios.post(url, requestPayload, { headers });
        return response.data;
    } catch (error) {
        // Show server error details if present
        if (error.response) {
            throw new Error(JSON.stringify(error.response.data));
        }
        throw new Error(error.message);
    }
}

// Example usage:
const payload = {
    key: "",
    integrationId: "765497ed-8710-48a0-a4d4-4a59b270f322",
    name: "Test Connection",
    additionalInfo: {},
    entityId: "test",
    authConfig: {}
};

createConnection(payload)
    .then(console.log)
    .catch(console.error);
