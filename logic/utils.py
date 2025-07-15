def process_button_input(current_expression: str, button_text: str) -> str:
    """
    Given the current expression string and a button label,
    return the updated expression string after processing.

    This mirrors the logic of _handle_button_click for non-control buttons.
    """
    if button_text == 'C':
        return ''
    if button_text == '=':
        # '=' is handled differently in UI, so just return the current expression
        return current_expression

    if button_text == '^':
        button_text = '**'
    elif button_text == '√':
        button_text = 'sqrt('
    elif button_text in ('sin', 'cos', 'tan', 'log', 'ln'):
        button_text += '('

    return current_expression + button_text
