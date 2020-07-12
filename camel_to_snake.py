def camel_to_snake_case(input_camel_string):
    output_snake_string = [input_camel_string[0].lower()]
    for i in input_camel_string[1:]:
        if i.isupper():
            output_snake_string.append('_')
            output_snake_string.append(i.lower())
        else:
            output_snake_string.append(i)
    return ''.join(output_snake_string)

if __name__ == '__main__':
    input_string = 'OnceUponATime'
    print(F"Input string in camel case: {input_string}")
    print(F"Output string snake in snake case: {camel_to_snake_case(input_string)}")
