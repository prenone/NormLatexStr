import math

def norm_latex_str(value, uncertainty, unit):
    # Calculate exponent and mantissa for uncertainty and value
    unc_exp = int(math.floor(math.log10(abs(uncertainty))))
    unc_man = uncertainty * 10 ** -unc_exp
    sig_digs = 2 if unc_man < 2 else 1
    unc_man_round = round(unc_man, sig_digs - 1)
    
    val_exp = int(math.floor(math.log10(abs(value))))
    val_man = value * 10 ** -val_exp
    val_man_round = round(val_man, sig_digs - 1 + (val_exp - unc_exp))
    
    unc_final = unc_man_round * 10 ** unc_exp
    val_final = val_man_round * 10 ** val_exp

    def fill_array(n):
        # Create an array with the integer and decimal parts placed correctly
        integer_part, _, decimal_part = str(n).partition('.')
        start_index = 32
        array = ['0'] * 64
        array[start_index - len(integer_part) + 1 : start_index + 1] = integer_part
        array[start_index + 1 : start_index + 1 + len(decimal_part)] = decimal_part
        return array

    array_unc = fill_array(unc_final)
    array_val = fill_array(val_final)
    
    # Remove leading zeros before the decimal point
    array_unc[:32] = ['' if el == '0' else el for el in array_unc[:32]]
    array_val[:32] = ['' if el == '0' else el for el in array_val[:32]]

    # Find the first significant digit index and trim unnecessary uncertainty digits
    first_sig_dig_index = next((i for i, el in enumerate(array_unc) if el not in ['', '0']), -1)
    array_unc[max(33, first_sig_dig_index + sig_digs):] = [''] * (64 - max(33, first_sig_dig_index + sig_digs))
    
    # Sync value array digits with the uncertainty array
    array_val[first_sig_dig_index:] = [
        val if unc != '' else '' 
        for val, unc in zip(array_val[first_sig_dig_index:], array_unc[first_sig_dig_index:])
    ]

    # Join the array to form the value and uncertainty strings
    val_str = (''.join(array_val[:33]) + '.' + ''.join(array_val[33:])).rstrip('.')
    unc_str = (''.join(array_unc[:33]).rstrip('.') + '.' + ''.join(array_unc[33:])).rstrip('.')
    
    return f"\\qty{{{val_str} \pm {unc_str}}}{{{unit}}}"

