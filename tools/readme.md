<img width="64" height="64" alt="image" src="https://github.com/user-attachments/assets/e2ca24e2-8289-4001-879f-81c40a8a4df9" />

EnvZero SoyBean Migrator
----
### How to use this

1. **Create an env0 API key & secret**  
   In env0, go to **Org Settings → API Keys** and create an API key and secret.  
   For more details, see the docs: https://docs.envzero.com

2. **Export environment variables**

    export ENV0_API_URL="https://api.env0.com"
    export ENV0_ORGANIZATION_ID="org-xxxx"
    export ENV0_API_KEY="..."
    export ENV0_API_SECRET="..."

3. **Run once in `DRY_RUN=True`**  
   Execute the script with `DRY_RUN = True` to see which templates will change, without applying any updates.

4. **Inspect a sample template**

    curl -H "Authorization: Basic <base64 key:secret>" \
         "https://api.env0.com/blueprints/<template-id>"

   Check the JSON response and adjust `TERRAFORM_TOOL_FIELD` in the script if needed.

5. **Apply changes**  
   Set `DRY_RUN = False` in the script and run it again to apply the updates.

---

**Extension**  
You can repeat the same pattern against the `/environments` endpoint if you have any **VCS-only environments** that are not based on templates and are still set to Terraform.
