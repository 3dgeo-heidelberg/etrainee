# h1 Heading

## h2 Heading

### h3 Heading

#### h4 Heading

##### h5 Heading

###### h6 Heading


## Emphasis

*This is italic text*

**This is bold text**


## Links

[link text](https://web.natur.cuni.cz/gis/etrainee)

## Images

Tool tip text can be added ("Team in VC")


<img src="module_template/media/telecon.jpg" alt="E-TRAINEE team photo" title="this will be displayed as a tooltip" width="200">

## Videos

These are only visible when rendering to html. Will check if they can be embedded in the markdown/git as well.

local, with relative path:
	
<iframe width="500" height="360" src="module_template/media/website_animation_3dgeo.mp4" frameborder="0" allowfullscreen></iframe>

online, e.g. from YouTube:
	
<iframe width="500" height="360" src="https://www.youtube.com/embed/4vqcFjbzJ8Q" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Blockquotes

> Blockquotes can also be nested...
>> ...by using additional greater-than signs right next to each other...
> > > ...or with spaces between arrows.


## Lists

Unordered

* Create a list by starting a line with `*`
* Sub-lists are made by indenting 2 spaces:
  - Marker character change forces new list start:
    + Facilisis in pretium nisl aliquet
* Very easy

Ordered

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa


## Code

Inline `code`

Block code "fences"

```
Sample text here...
```

Syntax highlighting

``` python
def foo(bar):
  return bar+=1

print(foo(3))
```

## Tables

| Option | Description |
| ------ | ----------- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |

## Equations 


3. Use Latex syntax for the equations in Markdown

Useful cheatsheet for Special characters/ Symbols: https://gist.github.com/LKS90/252ac41bd4a173be35b0

Example: 
``` python
$$ 
D = {k+1 \over {4 \over 3} \pi r{^3}_{kNN}} 
$$

$$ 
0 = d + n_x + n_x + n_z 
$$

$$
\lambda_3 \over {\lambda_1 + \lambda_2 + \lambda_3}
$$
```








