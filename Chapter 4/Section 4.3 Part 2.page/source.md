## Outcomes
After class time today you will be able to

* do more algebra in quotients of polynomial rings.

## Watch
<iframe title="embedded content" src="https://www.youtube.com/embed/_d_ZvuEXivs" width="560" height="315" allowfullscreen="allowfullscreen" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" data-mce-fragment="1"></iframe>

## Recommended practice
Go to <a class="" title="Link" href="https://sagecell.sagemath.org/" data-preview-alt="">SageCell</a> and use the following to produce the quotient ring \\(\\mathbb{Z}_{31}[x]/(x^3+2x^2+x+1)\\).
```
Z31 = Integers(31)<br>
R.<x> = Z31[]
S.<t> = R.quo(x^3+2*x^2+x+1)
```

* Add a line `t^4` after the line defining `S`, to see the representation of \\(t^4\\) in the set \\(\\{a_0+a_1t+a_2t^2 : a_0,a_1,a_2\\in\\mathbb{Z}_{31},\\ t^3+2t^2+t+1=0\\}\\).
* Use Sage to compute \\((\\overline{8x^2 + 11x + 19})(\\overline{14x^2 + 17x + 17}) = (8t^2+11t+19)(14t^2+17t+17)\\).