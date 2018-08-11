# Operational Calculus on Programming Spaces
A work in progress

## Abstract

In this work we present a theoretical model for differentiable programming. We present an algebraic language that enables both implementations and analysis of differentiable programs (of arbitrary order of differentition).

To this purpose, we develop an _abstract computational model of automatically differentiable programs_ of arbitrary order. In the model, programs are elements of op. cit. _programming spaces_ and are viewed as maps from a finite-dimensional vector space to itself op. cit. _virtual memory space_.
   Virtual memory space is also an algebra of programs, _an algebraic data structure_ one can calculate with.
   
We define the _operator of differentiation_ (∂) on programming spaces and, using its powers, implement the _general shift operator_ and the _operator of program composition_.
We provide the formula for the expansion of a differentiable program into an infinite tensor series in terms of the powers of ∂. We express the operator of program composition in terms of the generalized shift operator and ∂, which implements a differntiable composition in the language. We prove that our language enables differentiation of the derivatives of programs by the use of the _order reduction map_. We demonstrate our models algebraic power over analytic properties of differentiable programs by analysing iterators and their _iterating velocities_, and  solve the special case of _ReduceSum_.
