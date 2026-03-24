import os
from anthropic import Anthropic

# Make sure this env variable is actually set
print(os.environ.get("ANTHROPIC_API_KEY"))  # Should NOT print None

client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))