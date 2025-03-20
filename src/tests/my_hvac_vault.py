import hvac
from hvac.exceptions import InvalidPath

hvac_host = 'http://localhost:8200'
hvac_token = 'root'

client = hvac.Client(
    url=hvac_host,
    token=hvac_token
)


if client.is_authenticated():
    print("Vault authentication successful!")

for secret in ["my-secret", "our-secret", "your-secret"]:
    try:
        response = client.secrets.kv.v2.read_secret_version(path=secret, mount_point='secret')
        print(f"\n{response = }\n")
        print(response['data']['data'])  # Output the secret data
    except InvalidPath:
        response = None
        print(f"\nSecret {secret} not found!")


# Create secret with bash:
## vault kv put secret/my-secret my-value
### docker exec -it vault sh -c "export VAULT_ADDR=http://127.0.0.1:8200 && vault kv put secret/our-secret value=52"