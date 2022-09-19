<h2>Outcomes</h2>
<ul>
<li>After class time today you will be able to
<ul>
<li>do more algebra in quotients of polynomial rings.</li>
</ul>
</li>
</ul>
<h2>Preparation</h2>
<ul>
<li>Go to <a class="" title="Link" href="https://sagecell.sagemath.org/" data-preview-alt="">SageCell</a> and use the following to produce the quotient ring \(\mathbb{Z}_{31}[x]/(x^3+2x^2+x+1)\).<br>
<pre>Z31 = Integers(31)<br>
R.&lt;x&gt; = Z31[]<br>
S.&lt;t&gt; = R.quo(x^3+2*x^2+x+1)
</pre>
<ul>
<li>Add a line:
<pre>t^4</pre>
after the line defining S, to see the representation of <img class="equation_image" title="t^4" src="https://uweau.instructure.com/equation_images/t%255E4" alt="LaTeX: t^4" data-equation-content="t^4" x-canvaslms-safe-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;>
  <msup>
    <mi>t</mi>
    <mn>4</mn>
  </msup>
</math>"> in the set<br>\(\{a_0+a_1t+a_2t^2 : a_0,a_1,a_2\in\mathbb{Z}_{31},\ t^3+2t^2+t+1=0\}\).</li>
<li>Use Sage to compute \((\overline{8x^2 + 11x + 19})(\overline{14x^2 + 17x + 17}) = (8t^2+11t+19)(14t^2+17t+17)\).</li>
</ul>
</li>
<li></li>
</ul>