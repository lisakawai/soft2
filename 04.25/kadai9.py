(defun product (term a b)
  (if (> a b)
      1
    (* (funcall term a)
       (product term (+ a 1) b))))
product
(defun mul(a) (* a a a))
mul
(defun product-mul (a b)
  (product 'mul a b))
product-mul
(product-mul 1 5)
1728000
