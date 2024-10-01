
# **Valorant Agent Instalocker**

This is a Python-based Valorant Agent Instalocker that automatically locks your preferred agent during the agent select phase in Valorant. It connects to the Valorant API, reads your preferred agent from a configuration file, and provides an option to change agents dynamically via a console interface.

## Features
- Automatically selects and locks your preferred agent during agent select phase.
- Dynamically change the preferred agent via the console without needing to manually edit configuration files.
- Tracks locked matches to avoid trying to lock agents in the same match more than once.

## Requirements
- Python 3.x
- valclient library (for interacting with the Valorant API)


## Installation

Clone the repository:
```bash
  git clone https://github.com/Ivooooooooo/Valorant-Insta-Pick.git
  cd Valorant-Insta-Pick
```

Install the required dependencies:
```bash
  pip install valclient
```

Create a `config.json` file in the root of your project directory:
```json
{
  "instantlocker": {
    "enable_instantlocker": true,
    "askToChangeAgent": false,
    "region": "latam",
    "preferred_agent": "chamber"
  }
}
```
- **region**: Your game region (e.g., na, eu, ap).
- **preferred_agent**: The default agent you'd like to instalock (e.g., jett).

Create an `agents.json` file in the root directory, where all agent names and their respective IDs are stored:
```json
{
    "jett": "add6443a-41bd-e414-f6ad-e58d267f4e95",
    "reyna": "a3bfb853-43b2-7238-a4f1-ad90e9e46bcc",
    "raze": "f94c3b30-42be-e959-889c-5aa313dba261",
    "yoru": "7f94d92c-4234-0a36-9646-3a87eb8b5c89",
    "phoenix": "eb93336a-449b-9c1b-0a54-a891f7921d69",
    "neon": "bb2a4828-46eb-8cd1-e765-15848195d751",
    "breach": "5f8d3a7f-467b-97f3-062c-13acf203c006",
    "skye": "6f2a04ca-43e0-be17-7f36-b3908627744d",
    "sova": "320b2a48-4d9b-a075-30f1-1f93a9b638fa",
    "kayo": "601dbbe7-43ce-be57-2a40-4abd24953621",
    "killjoy": "1e58de9c-4950-5125-93e9-a0aee9f98746",
    "cypher": "117ed9e3-49f3-6512-3ccf-0cada7e3823b",
    "sage": "569fdd95-4d10-43ab-ca70-79becc718b46",
    "chamber": "22697a3d-45bf-8dd7-4fec-84a9e28c69d7",
    "omen": "8e253930-4c05-31dd-1b6c-968525494517",
    "brimstone": "9f0d8ba9-4140-b941-57d3-a7ad57c6b417",
    "astra": "41fb69c1-4189-7b37-f117-bcaf1e96f1bf",
    "viper": "707eab51-4836-f488-046a-cda6bf494859",
    "fade": "dade69b4-4f5a-8528-247b-219e5a1facd6",
    "gekko": "e370fa57-4757-3604-3648-499e1f642d3f",
    "harbor": "95b78ed7-4637-86d9-7e41-71ba8c293152",
    "deadlock": "cc8b64c8-4b25-4ff9-6e7f-37b4da43d235",
    "iso": "0e38b510-41a8-5780-5e8f-568b2a4f2d6c",
    "clove": "1dbf2edd-4729-0984-3115-daa5eed44993",
    "vyse": "efba5359-4016-a1e5-7626-b1ae76895940",
    "new_agent":"get from https://valorant-api.com/v1/agents"
}
```

Run the program:
```bash
python main.py
```

(Optional) Use Nuitka:
```bash
nuitka agentpick.py --onefile-no-compression
```

(Optional) Use VMProtect above Nuitka.

## Usage

- **Automatic Agent Selection**: The program will automatically select and lock the agent defined in the config.json during the agent select phase.
- **Change Agent During Match**: If you'd like to change your agent dynamically, the program will prompt you during the agent select phase. You can enter the new agent name from the available agents list, and it will lock that agent for the match.
- **Logs**: The program prints the current match ID and session state during execution and provides status messages for the agent select and lock processes.

## Troubleshooting
- Ensure that the Valorant game is running before executing the script.
- If the configuration file (`config.json`) or agents file (`agents.json`) is missing or malformed, the program will exit with an error. Check your files for proper formatting.
