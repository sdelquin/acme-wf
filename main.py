import subprocess
import crayons

from prettyconf import config

# settings
ACME_SH_PATH = config('ACME_SH_PATH')
ACME_WF_PATH = config('ACME_WF_PATH')
REDIRECT_PATH = config('REDIRECT_PATH')
DOMAINS = config('DOMAINS', cast=config.list)
WF_SERVER = config('WF_SERVER')
WF_USER = config('WF_USER')
WF_PASSWORD = config('WF_PASSWORD')


def run_cmd(cmd):
    print(crayons.white(cmd))
    subprocess.run(cmd, shell=True)


for domain, cert in [_.split('|') for _ in DOMAINS]:
    print(crayons.yellow('Handling'), crayons.white(domain, bold=True))
    print(crayons.magenta('Issue cert: '), end='')
    run_cmd(f'{ACME_SH_PATH} --issue -d {domain} -w {REDIRECT_PATH}')
    print(crayons.magenta('Install cert: '), end='')
    run_cmd(f'{ACME_SH_PATH} --install-cert -d {domain} \
    --reloadcmd "WF_SERVER={WF_SERVER} WF_USER={WF_USER} \
    WF_PASSWORD={WF_PASSWORD} WF_CERT_NAME={cert} python2.7 {ACME_WF_PATH}"')
