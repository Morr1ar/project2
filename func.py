def text_wrap(filename, window_size):

    text = ""
    text_list = [line.strip() for line in open(filename, encoding="utf-8").readlines()]
    if filename == 'instruction.txt':
        for i in range(1, len(text_list), 2):
            text += f'[ref={text_list[i]}]{text_list[i - 1]}[/ref]'
    else:
        if len(text_list) >= window_size:
            count = window_size
        else:
            count = len(text_list)
        for i in range(count):
            if len(text_list[i]) > window_size:
                x = 0
                while x < len(text_list[i]):
                    text += text_list[i][x:x + window_size] + '\n'
                    x += window_size
            else:
                text += text_list[i] + '\n'
    return text
