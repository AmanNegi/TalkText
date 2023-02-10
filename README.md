## TalkText ~ [GHW 2023(FEB)](https://ghw.mlh.io)
> [Demo Video]()

A simple Python project which uses `speech_recognition` and `datetime` library. The script simply listens for speech and stores it in a file.

## Execution Path

1. Initialize the `speech_recognition` object.
2. Listen for speech and convert it to text using `speech_recognition`.
3. Get the text and store it only if the user wants to. The file is named `output.txt`.
4. Repeat this process until the user agrees to the question, `Do you want to speak?` with `y`.

> To exit the program the user can simply type `n` and the program will stop execution.
