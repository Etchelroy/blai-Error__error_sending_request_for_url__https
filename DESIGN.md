This error means your computer can't reach Anthropic's servers to use Claude's API.

**Common causes:**
1. **No internet connection** — Check if you're actually online
2. **Firewall/VPN blocking** — Corporate network, security software, or VPN may be blocking the connection
3. **Invalid API key** — Wrong or expired key in your code
4. **DNS issues** — Your system can't resolve the domain name
5. **Server outage** — Rarely, Anthropic's servers are down (check status.anthropic.com)

**Quick fixes to try:**
- Restart your router
- Disable VPN temporarily and try again
- Check your API key is correct and has quotes around it
- Try `ping google.com` in terminal to confirm internet works
- If behind a corporate firewall, you may need a proxy configured

**If you're a developer:**
Share your code and I can check if the API request itself is formatted correctly. That might reveal the actual issue.