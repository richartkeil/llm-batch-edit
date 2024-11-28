# LLM Batch Edit

CLI tool using LLMs to apply an instruction to a list of files while considering the context of each file.

Useful if you have a list of files that all require a similar change, but differ in ways that would usually require manual processing.

Be aware that the tool changes files in place, so ideally you have version control setup. This makes it also easy to proof-read the changes before committing them.

## Usage

Install the package with `pip install .` or `pip install -e .` for development.

Make sure to store your OpenAI API key in an `OPENAI_API_KEY` environment variable.

```sh
Usage: llm-batch-edit [OPTIONS]

  Apply a change to a list of files, powered by OpenAI's LLMs.

Options:
  -l, --filelist PATH          File containing a list of filenames to apply the change to.  [required]
  -i, --instruction TEXT       Instruction to follow.  [required]
  -o, --example_original PATH  File containing an example of an original file. [required]
  -c, --example_changed PATH   File containing an example of the changed original file.  [required]
  -m, --model TEXT             OpenAI model to use for the change.
  --help                       Show this message and exit.
```

## Example

In the `example/src` directory we have three files that all contain a function with a number in its name. We want to extend a print statement in each function so that it also prints the next number after the one referenced in the function name. Basically just a task that would be hard to automate with normal refactoring tools.

Therefore, we can simply prepare an example of the original file (`example/original.py`) and an example of the changed file (`example/changed.py`), add all the files that should be changed to a list (`example/filelist`) and run the following command:

```sh
llm-batch-edit \
    --filelist ./example/filelist \
    --instruction "In the print statement, add (next number is X) where X is the next number after the one referenced in the function name" \
    --example_original ./example/original.py \
    --example_changed ./example/changed.py
```

### Roadmap

- add option to only pass relevant file parts to llm (e.g. diff of original and changed file) to reduce cost and time
- add groq API support for faster + cheaper inference
- nicer cli progress (e.g. spinner + progress bar)
