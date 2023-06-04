import os
import openai
import argparse
import re

api_key = "open_api_key here"
openai.api_key = api_key


def summarize_code(code):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Can you summarize this code? \n\n {code}"},
        ]
    )

    return response['choices'][0]['message']['content']


def read_code_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        code = file.read()
    return code




def infer_usage(code):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"\nHow to run the following code in the terminal: {code}\n",
        temperature=0.5,
        max_tokens=300
    )

    return response.choices[0].text.strip()



def check_openai_usage(code):
    return 'openai' in code


def write_readme(summary, usage,  openai_used):
    with open('README.md', 'w') as file:
        file.write('## :space_invader: About\n\n')
        file.write(f'{summary}\n\n')

        if openai_used:
            file.write('## :rocket: OpenAI API\n\n')
            file.write('This application uses the OpenAI API. You will need to obtain an API key from the [OpenAI website](https://openai.com/)')
        file.write('## :runner:  Usage\n\n')
        file.write(usage)
        file.write('\n\n')
        file.write('\n\n')
        file.write('\n\n')


def main():
    parser = argparse.ArgumentParser(description='Summarize the given code.')
    parser.add_argument('file_path', type=str, help='The path to the code file to summarize.')

    args = parser.parse_args()
    code = read_code_from_file(args.file_path)
    summary = summarize_code(code)
    usage = infer_usage(code)
    openai_used = check_openai_usage(code)

    write_readme(summary, usage, openai_used)
    print("README.md file has been generated.")


if __name__ == "__main__":
    main()
