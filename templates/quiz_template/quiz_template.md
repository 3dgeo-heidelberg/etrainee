# Etrainee template quiz

## Markdown before HTML code

This template provides everything necessary to create a self-evaluating quiz.
Hopefully, there are no limitations on the number of created questions.
Every quiz needs to be enclosed in the `<form>` tag and please also include the `<input type="submit">` and `<output id="output_overall">` tags at the end of the form.
Individual questions have this general structure:

```
<!--Question --question number-- -->    
<label for="q_--question number--">
    --Text of the question--
</label><br>
<input type="--question type--" name="q_--question number--"><br>

<div id="correct_q_--question number--" hidden="">

--The correct answer--

</div>

<output id="output_q_--question number--">
</output>
    
<br><br>   
```
At the beginning of a quiz include: (property name="quiz" has been added in April 2023)
```
<form name="quiz" action="" method="post" onsubmit="evaluate_quiz(); return false">
```
All appearances of `--question number--` should be replaced by the same number.
Structure of the `<input>` tag depends on the type of question you want to create:

1. **Text** type questions can be created by using either the `<input type="text">` or `<textarea>` tags (`<textarea rows = "5" cols = "50" name = "q_--question number"></textarea><br>`)

2. **Radio** type questions are created by defining as many `<input type="radio">` elements,
as we want to have possible answers.
General structure of one individual radio button should be similar to this: `<input type="radio" name="q_--question number--">--answer--`

3. **Range/slider** type questions are created using a single `<input type="range">`
tag structured in this way: `--min value--<input type="range" min=--min value-- max=--max value-- step=--step value-->--max value--`

4. **Matching** type questions are created as two separate tables. First table contains `<select>` elements with the corresponding value.
Second table contains the answers to be matched with values from the first table. 
All `<select>` elements corresponding to a single question need to have the same name and individual options
are added using `<option>` tags. Overall, a matching type question should adhere to this structure:
```
<label for="q_--question number--">
	--Text of the question--
</label><br>
<table>
<tr>
	<td>
		<select name="q_--question number--">
			<option></option>
			<option>--possible answer--</option>
			...
			<option>--possible answer--</option>
		</select>
		--text of the corresponding answer in the first column--
	</td>
	<td>
		--another select and text--
	</td>
</tr>
<tr>
	...
</tr>
</table>

<table>
tr>
	<td>--one answer--</td>
	<td>--second_answer--</td>
	...
</tr>
<tr>
	...
</tr>
</table>

<div id="ccorrect_q_--question number--" hidden="">

--The correct answer--

</div>

<output id="output_q_--question number--">
</output>
    
<br><br>   
```
At the end of a quiz include:
```
<input type="submit" value="Submit" style="font-size:14pt"><br><br>

<output id="output_overall">
</output>
</form>
```

### Quiz evaluation

The quiz is evaluated by a script located at `course\assets\javascripts\quiz_evaluation.js`. The javascript file is automatically included when building the site by including
```
extra_javascript:
    - assets\javascripts\quiz_evaluation.js
```
in the `mkdocs.yml` file.
	
Good luck creating quizzes!

## Quiz

<form name="quiz" action="" method="post" onsubmit="evaluate_quiz(); return false">

<!--Question 1-->
<label for="q_01">
What does SAR stand for?
</label><br>
<textarea rows = "5" cols = "50" name = "q_01"></textarea><br>
<div hidden id="correct_q_01">Synthetic Aperture Radar</div>
<output id="output_q_01"/></output><br><br>

<!--Question 2-->
<label for="q_02">
------------------------------------?
</label><br>
<textarea rows = "5" cols = "50" name = "q_02"></textarea><br>
<div hidden id="correct_q_02">Hello World!</div>
<output id="output_q_02"/></output><br><br>

<!--Question 3-->
<label for="q_03">
---------------------------------------------?
</label><br>
<textarea rows = "5" cols = "50" name = "q_03"></textarea><br>
<div hidden id="correct_q_03">true</div>
<output id="output_q_03"></output><br><br>

<!--Question 4-->
<label for="q_04">
-----?
</label><br>
1<input type="range" name="q_04" min="1" max="5", step="1">5<br>
<div hidden id="correct_q_04">5</div>
<output id="output_q_04"></output><br><br>

<!--Question 5-->
<label for="q_05">
How many--------------?
</label><br>
<input type="radio" name="q_05">1
<input type="radio" name="q_05">2
<input type="radio" name="q_05">3
<input type="radio" name="q_05">4
<input type="radio" name="q_05">5<br>
<div hidden id="correct_q_05">2</div>
<output id="output_q_05"></output><br><br>

<!--Question 6-->
<label for="q_06">
--------------?
</label><br>
<input type="radio" name="q_06">Longer text answer<br>
<input type="radio" name="q_06">Hello world!<br>
<input type="radio" name="q_06">Lorem ipsum dolor sit amet,
consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.<br>
<input type="radio" name="q_06">Is this correct?<br>
<input type="radio" name="q_06">Or even this?<br>
<div hidden id="correct_q_06">Hello world!</div>
<output id="output_q_06"></output><br><br>

<!--Question 7-->
<label for="q_07">
Which option corresponds to which?
</label><br>
<!--1st table - contains select elements-->
<table>
<tr>
	<td><select name="q_07"> 
		<option></option>	<!--default option-->
		<option>A</option>
		<option>B</option>
		<option>C</option>
		<option>D</option>
		<option>E</option>
	</select>
	1. Sentinel-1</td>
	<td><select name="q_07"> 
		<option></option>
		<option>A</option>
		<option>B</option>
		<option>C</option>
		<option>D</option>
		<option>E</option>
	</select>
	2. Sentinel-2</td>
	<td><select name="q_07"> 
		<option></option>
		<option>A</option>
		<option>B</option>
		<option>C</option>
		<option>D</option>
		<option>E</option>
	</select>
	3. Sentinel-3</td>
</tr>
<tr>
	<td><select name="q_07"> 
		<option></option>
		<option>A</option>
		<option>B</option>
		<option>C</option>
		<option>D</option>
		<option>E</option>
	</select>
	4. Sentinel-5P</td>
	<td><select name="q_07"> 
		<option></option>
		<option>A</option>
		<option>B</option>
		<option>C</option>
		<option>D</option>
		<option>E</option>
	</select>
	5. Sentinel-6</td>
	<td></td>
</tr>
</table>

<!--2nd table - contains corresponding answers-->
<table>
<tr>
	<td>A. Land optical</td>
	<td>B. Atmosphere</td>
	<td>C. SAR C-Band</td>
</tr>
<tr>
	<td>D. Ocean altimetry</td>
	<td>E. Ocean optical</td>
	<td></td>
</tr>
</table><br>
<div hidden id="correct_q_07">C A E B D</div>
<output id="output_q_07"></output><br><br>

<input type="submit" value="Submit" style="font-size:14pt"><br><br>

<output id="output_overall"></output>

</form>

## Markdown after HTML code

This is just to show that markdown text can also be used after the html-based quiz.