# formation-python-HUG-API-and-Ionic-Svelte
Formation 'Python REST API et Ionic Svelte'  par Miguel Monwoo

## Installation (MacOS)

```bash

python3 -m venv .venv
source .venv/bin/activate

# https://sixfeetup.com/blog/end-to-end-testing-python-playwright
pip3 install pytest-playwright
pip3 install hug -U

# Launch functional or
export URL=https://demo.mediacms.io
python first_test.py

```
## Dev launch (MacOS)

```bash
source .venv/bin/activate
hug -f first_step_2.py

# DDD : run clients tests check automatic validation
./serveur-api/e2e.sh

```
