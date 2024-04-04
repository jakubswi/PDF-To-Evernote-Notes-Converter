# PDF to Evernote Notes Converter

This project is a Python script designed to extract text from a PDF file, convert it into a readable format suitable for
note-taking, and then enhance it using AI-generated suggestions. The final output is intended to be formatted nicely for
applications like Evernote, where users can efficiently organize and store their notes.

## Dependencies

- Python 3.x
- `requests` library (install via `pip install requests`)
- Ilovepdf API key (obtainable from [ilovepdf.com](https://www.ilovepdf.com/api))
- OpenAI API key (obtainable from [OpenAI](https://openai.com/))

## Usage

1. Clone this repository to your local machine.
2. Ensure Python and the required dependencies are installed.
3. Set up environment variables for your Ilovepdf and OpenAI API keys. You can do this by exporting them in your
   terminal session or setting them in your IDE/environment.
4. Place the PDF file you want to convert in the `Input` directory and name it `merged.pdf`.
5. Run the script by executing `python pdf_to_evernote.py`.
6. Once the script completes, you'll find the formatted notes in the `Output` directory as `processed_file.txt`.

## Configuration

- Ensure your Ilovepdf API key is stored as an environment variable named `ILOVEPDF_KEY`.
- Ensure your OpenAI API key is stored as an environment variable named `OPEN_AI_KEY`.

## Notes

- The script uses the Ilovepdf API to extract text from the PDF file.
- It then utilizes the OpenAI API to enhance the extracted text for better readability and organization.
- The final output is a text file (`output.txt`) that you can import into Evernote or any other note-taking
  application.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to customize the script to suit your specific requirements or integrate it into your workflow as needed!