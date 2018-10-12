# Operational Calculus for Differentiable Programming
Repository for the paper Operational Calculus for Differentiable Programming

## Abstract

In this work we present a theoretical model for differentiable programming. We
construct an algebraic language that encapsulates formal semantics of differentiable programs by way of _Operational Calculus_. The algebraic nature of Operational Calculus can alter the properties of the
programs that are expressed within the language and transform them into their solutions.

In our model programs are elements of _programming spaces_ and viewed
as maps from the _virtual memory space_ to itself. Virtual memory space is an algebra of programs, _an algebraic data structure_ one can calculate with.  We define the _operator of differentiation_ (`∂`) on programming spaces and, using its powers, implement the _general shift operator_ and the _operator of program composition_. We provide the formula for the
expansion of a differentiable program into an infinite tensor series in terms of the powers of `∂`. We express the operator of program composition in terms of the generalized shift operator and `∂`, which implements a differentiable composition in the language. Such operators serve as abstractions
over the tensor series algebra, as main actors in our language.  

We demonstrate our models usefulness in differentiable programming by using it to analyse iterators, deriving _fractional iterations_ and their _iterating velocities_, and explicitly solve the special case of _ReduceSum_.

### Compiling the paper

In order to compile the paper from source run the `compile.py` script. Consult its help by running `compile.py --help` if needed.

