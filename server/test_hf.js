require('dotenv').config();
const { HfInference } = require('@huggingface/inference');
const dns = require('dns');

// Fix 1: Force IPv4 first (common fix for Node 17+ ENOTFOUND errors)
try {
    dns.setDefaultResultOrder('ipv4first');
    console.log("Set default DNS result order to ipv4first");
} catch (e) {
    console.log("Could not set default DNS result order (older Node version?)");
}

const token = process.env.HF_API_TOKEN;
const hf = new HfInference(token);

async function run_diagnostics() {
    console.log("--- DNS DIAGNOSTICS ---");
    try {
        const addresses = await dns.promises.resolve('huggingface.co');
        console.log("Resolved addresses:", addresses);
    } catch (e) {
        console.error("DNS Lookup failed:", e.code, e.message);
    }

    const hf = new HfInference(process.env.HF_API_TOKEN);

    console.log("\n--- TEST 1: gpt2 (Basic HF API) ---");
    try {
        const res1 = await hf.textGeneration({
            model: 'gpt2',
            inputs: 'Hello',
            parameters: { max_new_tokens: 5 }
        });
        console.log("GPT2 Success!", res1.generated_text);
    } catch (e) {
        console.error("GPT2 Failed:", e.message);
    }

    console.log("\n--- TEST 2: gemma-3-27b-it (Chat Completion) ---");
    try {
        const res2 = await hf.chatCompletion({
            model: 'google/gemma-3-27b-it',
            messages: [{ role: 'user', content: 'Hello, are you a doctor?' }],
            max_tokens: 50
        });
        console.log("Gemma Success!"); 
        console.log("Response:", res2.choices[0].message.content);
    } catch (e) {
        console.error("Gemma Failed:", e.message);
        console.error("Cause:", e.cause);
    }
}

run_diagnostics();
