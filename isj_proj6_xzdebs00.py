#!/usr/bin/env python3

class Polynomial:
    """
    A class used to make Polynomial

    Attributes
    ----------
    poly: list
        representation of polinomial using indexes

    Methods
    -------
    str():
        Returns polynomial in the usual form.
    '==':
        Result of comparison two polynomials.
    '+':
        Returns sum of two polynomials.
    '*':
        Returns the result of multiplying 2 polynomials.
    '**':
        Returns the result of exponentiation of a polynomial.
    derivative()
        Returns differentiated polynomial.
    at_value(constant_1, constant_2 = None)
        Returns the value of the polynomial for the given x.
    """
    def __init__(self,*args,**kwargs):
        """
        Parameters
        ----------
        args: sequence of indexes
        args[0]: list of indexes
        kwargs: keyword indexes
        """
        if len(args) > 1: #sequence as argument
            self.poly = list(args)
        elif len(args) == 1: #list as argument
            self.poly = args[0] if isinstance(args[0], list) else [args[0]]
        else: #dictionary as argument
            list_keys = list(kwargs.keys())
            # find max index near x
            maxkey = max([ int(key[1:]) for key in list_keys ])
            # initiates an array with 0 of n, where n is the biggest x plus 1
            self.poly = [0]*(maxkey+1)
            for key in list_keys:
                self.poly[int(key[1:])] = kwargs[key] #changing value in x index from 0 to given

        #removes all 0 at the end of list
        while len(self.poly) > 1:
            if self.poly[-1] == 0:
                self.poly.pop()
            else:
                break

    def __str__(self):
        """Returns polynomial in the usual form.

        Returns
        -------
        str
            A string displaying a polynomial in the usual form.

        Example
        -------
        Polynomial(0,1,0,-1,4,-2,0,1,3,0) >> "3x^8 + x^7 - 2x^5 + 4x^4 - x^3 + x"
        """
        res_str = "" #resulting string
        for i in range(len(self.poly)-1, -1, -1):

            # check whether to write 0 elem
            if self.poly[i] == 0 and len(self.poly) != 1:
                continue

            # adding sign without 1 elem
            if i != len(self.poly)-1:
                if self.poly[i] > 0:
                    res_str += " + "
                else:
                    res_str += " - "
            
            # adding index near x if it needed
            # there are exeptions like 1 we dont need near x, but it could be as elem
            # also as exeption 0 polynomial
            if abs(self.poly[i]) != 1 or (abs(self.poly[i]) == 1 and i == 0) \
                or (self.poly[i] == 0 and len(self.poly) == 1):
                res_str += str((abs(self.poly[i])))

            # adding x with possible power
            if i == 1:
                res_str += "x" #the first degree is not displayed
            elif i!=0: 
                res_str += f"x^{i}"

        return res_str

    def __eq__(self, poly_2):
        """Result of comparison two polynomials.

        Parameters
        ----------
        poly_2 : Polynomial
            second polynomial

        Returns
        -------
        Boolean
            Returns True if the polynomials are equal, and False - if not.
        """
        return self.poly == poly_2.poly

    def __add__(self, poly_2):
        """Returns sum of two polynomials.

        Parameters
        ----------
        poly_2 : Polynomial
            second polynomial

        Returns
        -------
        Polynomial
            Result of summing two polynomials.
        """
        poly_1 = self #to leave unchangeed
        #making lists the same size
        poly_2.poly.append([0]*len(poly_1.poly)-len(poly_2.poly))
        poly_1.poly.append([0]*len(poly_2.poly)-len(poly_1.poly))
        return Polynomial(list(map(sum, zip(poly_1.poly, poly_2.poly))))

    # addition func for power
    def __mul__(self, poly_2):
        """Returns the result of multiplying 2 polynomials.

        Parameters
        ----------
        poly_2 : Polynomial
            second polynomial

        Returns
        -------
        Polynomial
            Result of multiplying two polinomials.
        """
        res_poly = [0]*(len(self.poly)+len(poly_2.poly)-1) #filling list with 0 of n, where n is a res pow
        for i_1,num_1 in enumerate(self.poly):
            for i_2,num_2 in enumerate(poly_2.poly):
                res_poly[i_1+i_2] += num_1*num_2
        return Polynomial(res_poly)

    def __pow__(self, constant):
        """Returns the result of exponentiation of a polynomial.

        Parameters
        ----------
        constant : int
            the power to which the polynomial must be raised

        Returns
        -------
        Polynomial
            Returns the polynomial raised to the given power.
        """
        res_polynomial = self
        for i in range(constant-1):
            res_polynomial *= self 
        return res_polynomial
    
    def derivative(self):
        """Returns the differentiated polynomial.

        Returns
        -------
        Polynomial
            Result of polynomial differentiation.
        """
        # resulting zero polynomial as exeption
        if len(self.poly) == 1: 
            return Polynomial(0)

        res_poly = [0]*(len(self.poly)-1)
        for i in range(1, len(self.poly)):
            res_poly[i-1] = self.poly[i]*i
        return Polynomial(res_poly)

    def at_value(self, constant_1, constant_2 = None):
        """Returns the value of the polynomial for the given x.

        Parameters
        ----------
        constant_1 : int
            constant value for x
            
        constant_2 : int, optional
            second constant value for x (default is None)

        Returns
        -------
        float
            Returns the value of the polynomial for the given perameter.
            If 2 values are specified, the result is the difference 
            between the at_value() value of the second and first parameters
        """
        return  (sum(num * constant_2 ** i for i,num in enumerate(self.poly)) - 
            sum(num * constant_1 ** i for i,num in enumerate(self.poly))) \
                if constant_2 else sum(num * constant_1 ** i for i,num in enumerate(self.poly))
