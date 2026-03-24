This error means your request to Anthropic's API failed at the network level. Common causes:

1. **No internet connection** — Check your network
2. **Firewall/proxy blocking** — Corporate network might block the API endpoint
3. **DNS issues** — Can't resolve api.anthropic.com
4. **Anthropic API is down** — Check [status.anthropic.com](https://status.anthropic.com)
5. **Invalid API key** — If misconfigured, connection fails before auth
6. **Rate limiting** — Too many requests too fast (returns 429, but sometimes manifests as connection error)
7. **TLS/SSL certificate issue** — Rare, but outdated system certs can cause this

**Quick fixes:**
- Restart your internet connection
- Try a different network (mobile hotspot, different WiFi)
- Check if you can ping `api.anthropic.com` from terminal
- Verify your API key is set correctly in environment variables
- Try again in a few minutes (might be temporary downtime)

If this is happening in a specific app or tool, share the code/context and I can help debug further.