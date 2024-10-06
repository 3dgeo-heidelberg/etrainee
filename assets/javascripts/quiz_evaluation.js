function log_answers() {
	// returns a dictionary with all submitted answers

	// create dictionary to hold submitted answers
	var ans_dict = {}
	var q_types = {}
	
	// go through all form elements
	for (var element of document.forms.quiz) {

		// add new entry to dict if key not yet present
		if (!Object.keys(ans_dict).includes(element.name)) {
			
			// add question type to q_types dict
			q_types[element.name] = element.type
			
			// add entry to ans_dict based on element type
			switch(element.type) {
			case "radio":
				var element_name = element.name
				// check if there is a selected radio button
				if (document.querySelector('input[name='+element_name+']:checked') !== null){
					// assign value if a button is selected
					var element_radio_val = document.querySelector('input[name='+element_name+']:checked').nextSibling.data
					ans_dict[element.name] = element_radio_val
				} else {
					// assign empty string if button not selected
					ans_dict[element.name] = ""
				}
				break;
			case "select-one":
				var element_name = element.name
				// select all elements with a given name
				var node_list = document.querySelectorAll("select[name="+element_name+"]");
				
				// gather all selected values into a string
				var out_str = ""
				for (var node of node_list) {
					out_str = out_str + " " + node.selectedOptions[0].innerText
				}
				ans_dict[element.name] = out_str
				break;
			case "textarea":
				ans_dict[element.name] = element.value
				break;
			case "text":
				ans_dict[element.name] = element.value
				break;
			case "range":
				ans_dict[element.name] = element.value
				break;
			case "checkbox":
				var element_name = element.name
				var node_list = document.querySelectorAll("input[name="+element_name+"]:checked");
				// gather all selected values into a string
				var out_str = ""
				for (var node of node_list) {
					out_str = out_str + "&" + node.nextSibling.data
				}
				ans_dict[element.name] = out_str
				break;
			case "submit":
				break;
			case "output":
				break;
			}
		}
	}
	return [ans_dict, q_types]
}

function collect_answer_elements() {
	//collects elements where answers are displayed
	
	// dict for collecting elements
	var out_dict = {}

	// loop through all form elements
	for (var element of document.forms.quiz) {
		// check if element is used for output
		if (element.type == "output") {
			out_dict[element.id] = element
		}
	}
	return out_dict
}

function log_correct(ans_dict) {
	// collects correct answers from hidden divs
	
	// dict for collecting correct answers
	var out_dict = {}

	// loop through all form elements
	for (var key of Object.keys(ans_dict)) {
		// check if element is used for output
		var new_key = "correct_" + key
		var correct = document.getElementById(new_key).textContent
		out_dict[new_key] = correct
	}
	return out_dict
}

function check_answer(user, correct) {
	// checks if answers are correct
	// santise input
	var user_norm = user.toLowerCase().trim()
	var correct_norm = correct.toLowerCase().trim()
	
	// if answer is correct
	return  user_norm == correct_norm
}

function check_answer_multiple_choice(user, correct) {
	// checks if answers are correct
	var correct_temp = structuredClone(correct)
	var num_correct = 0
	for (var user_ans of user) {
		if (correct_temp.includes(user_ans)) {
			var drop_idx = correct_temp.indexOf(user_ans)
			correct_temp.splice(drop_idx, 1)
			num_correct = num_correct + 1
		}
	}
	// is answer correct?
	if (num_correct == correct.length && num_correct == user.length-1) {
		return "correct"
	// is answer wrong?
	} else if (num_correct == 0) {
		return "wrong"
	// otherwise it is partially correct
	} else {
		return "partially"
	}
}

function format_correct_list(in_list) {
	if (in_list.length > 1) {
		var out_str = ' the correct answers are "' + in_list.join('" and "') + '"'
	} else {
		var out_str = ' the correct answer is "' + in_list + '"'
	}
	return out_str
}

function eval_multiple_choice(ans, out_element, ans_count, correct_list) {
	var correct_str =  format_correct_list(correct_list)
	switch(ans) {
		case "correct":
			ans_count["correct"] = ans_count["correct"] + 1
			out_element.value = "Correct"
			out_element["style"] = "background-color: #7DCEA0; padding: 3pt 15pt;"
			break;
		case "partially":
			ans_count["partially"] = ans_count["partially"] + 1
			out_element.value = "Your answer was partially correct," + correct_str
			out_element["style"] = "background-color: #F7DC6F; padding: 3pt 15pt;"
			break;
		case "wrong":
			ans_count["wrong"] = ans_count["wrong"] + 1
			out_element.value = "Sorry," + correct_str
			out_element["style"] = "background-color: #F1948A; padding: 3pt 15pt;"
			break;
	}
}

function display_messages(answers, answers_correct, answer_elements, q_types) {
	// displays messages
	// go through individual answers
	var ans_count = {correct:0, wrong:0, partially:0}
	
	for (var [key, value] of Object.entries(answers)) {
		// get correct answer
		var value_correct = answers_correct["correct_" + key]

		// get output element
		var out_element = answer_elements["output_" + key]

		// check answer
		// is the question answered?
		if (value.trim() == "") {
			out_element.value = "Please add an answer"
			out_element["style"] = "background-color: #F7DC6F; padding: 3pt 15pt;"
		// Is the question an open ended text?
		} else if (q_types[key] == 'text' || q_types[key] == 'textarea') {
			out_element.value = 'Consider if your answer aligns with our: ' + value_correct
			out_element["style"] = "background-color: #D7DBDD; padding: 3pt 15pt;"
		// Was this a multiple choice question? - evaluate how corect it was
		} else if (q_types[key] == 'checkbox') {
			// convert answer strings to arrays
			var value_parts = value.split("&");
			var value_correct_parts = value_correct.split("&");
			// Check how correct was the answer
			var checked_multiple_choice = check_answer_multiple_choice(value_parts, value_correct_parts)
			// display message based on correctness
			eval_multiple_choice(checked_multiple_choice, out_element, ans_count, value_correct_parts)
		// is the answer correct?
		} else if (check_answer(value, value_correct)) {
			ans_count["correct"] = ans_count["correct"] + 1
			out_element.value = "Correct, the answer is " + value_correct
			out_element["style"] = "background-color: #7DCEA0; padding: 3pt 15pt;"
		// Wrong answers
		} else {
			ans_count["wrong"] = ans_count["wrong"] + 1
			out_element.value = "Sorry, the correct answer is " + value_correct
			out_element["style"] = "background-color: #F1948A; padding: 3pt 15pt;"
		}
	}
	display_overall(ans_count)
}

function display_overall(ans_dict) {
	// display the overall results
	
	// get the output element and set its style
	var overall_element = document.getElementById("output_overall")
	overall_element["style"] = "background-color: #D7DBDD; padding: 3pt 15pt;"
	// compute the number of answered questions
	var answered_questions = ans_dict["correct"] + ans_dict["wrong"] + ans_dict["partially"]
	
	// Display different messages based on how many questions the user got wrong
	if (ans_dict["wrong"] + ans_dict["partially"] < 3) {
		overall_element.value = "Congratulations, you had " + ans_dict["correct"] + " answers correct out of " + answered_questions + " answered questions."
	} else {
		overall_element.value = "You had " + ans_dict["correct"] + " answers correct out of " + answered_questions + " answered questions, please consider reviewing the relevant sections again."
	}
}

function evaluate_quiz() {
	// log user answers
	var [answers, q_types] = log_answers()

	// log correct responses
	var ans_correct = log_correct(answers)

	// collect elements for answers
	var ans_elements = collect_answer_elements()
	
	display_messages(answers, ans_correct, ans_elements, q_types)
	
	//console.log(answers)
	//console.log(ans_correct)
	//console.log(ans_elements)
}