# LLM Bulk Change

CLI tool using LLMs to apply an instruction to a list of files while considering the context of each file.

Useful if you have a list of files that all require a similar change, but differ in ways that would usually require manual processing.

## Usage

Install the package with `pip install .` or `pip install -e .` for development.

Make sure to store your OpenAI API key in an `OPENAI_API_KEY` environment variable.

```sh
Usage: llm-bulk-change [OPTIONS]

  Apply a change to a list of files, powered by OpenAI's LLMs.

Options:
  -l, --filelist PATH          File containing a list of filenames to apply the change to.  [required]
  -i, --instruction TEXT       Instruction to follow.  [required]
  -o, --example_original PATH  File containing an example of an original file. [required]
  -c, --example_changed PATH   File containing an example of the changed original file.  [required]
  -m, --model TEXT             OpenAI model to use for the change.
  --help                       Show this message and exit.
```
