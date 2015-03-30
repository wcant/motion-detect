%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)

<p><h3>Detects:</h3></p>
<table border="1">
	<tr>
		<td>ID</td>
		<td>Day</td>
		<td>Day#</td>
		<td>Month</td>
		<td>Year</td>
		<td>Hour</td>
		<td>Minute</td>
		<td>Second</td>
		<td>Img</td>
	</tr>
%for row in rows:
  %id, day, dayn, mon, year, hour, minu, sec, img_name = row
	%img_name = "<a href="+"\'/images/"+img_name+"\'> Image </a>"
	%row = [id, day, dayn, mon, year, hour, minu, sec, img_name]	
	<tr>
  %for col in row:
    <td>{{!col}}</td>
  %end
  </tr>
%end
</table>

