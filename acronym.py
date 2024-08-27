import typer
from typing_extensions import Annotated


def get_acronym(input_string: str) -> str:
    """
    Convert a raw string to acronym string
    """

    # split string to words
    words = input_string.split()

    # collect the first character of each word and convert them to upper case
    initial_letters = [word[0].upper() for word in words]

    # get acronym result
    acronym = "".join(initial_letters)

    return acronym


def main(
    input_file: Annotated[str, typer.Argument(help="input text file for process")],
    output_file: Annotated[str, typer.Argument(help="output file to store the result")],
):
    """
    Read each line from input_file, convert them into acronym, store the result to output_file
    """

    # store the acronym strings
    line_result = []

    # read each line in the input file, then process it
    with open(input_file, "r") as input_fd:
        for line in input_fd:
            # do some cleaner work
            clean_line = line.strip()

            # get acronym
            line_acronym = get_acronym(clean_line)

            # add to result collection
            line_result.append(line_acronym)

    # write result to the output file
    with open(output_file, "w") as output_fd:
        # convert the result to file content
        file_content = "\n".join(line_result)

        # write it to file
        output_fd.write(file_content)


if __name__ == "__main__":
    typer.run(main)
