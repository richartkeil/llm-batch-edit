import os
import click
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()


def apply_change(filename, instruction, example_original, example_changed, model):
    with open(filename, "r") as file:
        file_original = file.read()

    system_message = {
        "role": "system",
        "content": "You are a helpful refactoring assistant. You only output the raw content.",
    }
    user_message = {
        "role": "user",
        "content": f"""
Here is an example of an original file:
```
{example_original}
```

Here is the instruction that should be followed:
```
{instruction}
```

Here is the original example, but with the instruction followed and changes applied:
```
{example_changed}
```

Transform the following file in a similar way by following the instruction.
Directly output the WHOLE changed file, DO NOT output anything else.
```
{file_original}
```""",
    }

    response = client.chat.completions.create(
        model=model, messages=[system_message, user_message]
    )
    output = response.choices[0].message.content
    tokens = response.usage.total_tokens

    with open(filename, "w") as file:
        file.write(output.strip("`").strip() + "\n")

    print(f"Applied change to {filename} ({tokens} Tokens).")


@click.command()
@click.option(
    "-l",
    "--filelist",
    required=True,
    help="File containing a list of filenames to apply the change to.",
    type=click.Path(exists=True),
)
@click.option(
    "-i",
    "--instruction",
    required=True,
    prompt="Instruction to be followed for a file",
    help="Instruction to follow.",
)
@click.option(
    "-o",
    "--example_original",
    required=True,
    help="File containing an example of an original file.",
    type=click.Path(exists=True),
)
@click.option(
    "-c",
    "--example_changed",
    required=True,
    help="File containing an example of the changed original file.",
    type=click.Path(exists=True),
)
@click.option(
    "-m", "--model", default="gpt-4", help="OpenAI model to use for the change."
)
def run(filelist, instruction, example_original, example_changed, model):
    """Apply a change to a list of files, powered by OpenAI's LLMs."""
    with open(filelist, "r") as file:
        filelist = file.readlines()
    with open(example_original, "r") as file:
        example_original = file.read()
    with open(example_changed, "r") as file:
        example_changed = file.read()

    for line in filelist:
        filename = line.strip()
        if not os.path.isfile(filename):
            print(f"File {filename} does not exist.")
            continue
        apply_change(filename, instruction, example_original, example_changed, model)
