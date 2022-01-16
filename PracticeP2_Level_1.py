def bracket_pattern(input_str):
	if input_str.startswith("(") and input_str.endswith(")"):
	    if input_str.count("(")==input_str.count(")"):
	        return True
	return False

    
input_str="(())("
print(bracket_pattern(input_str))
