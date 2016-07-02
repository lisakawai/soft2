(defun sum-squares (a b)
  (if (> a b)
      0
    (+ (* a a) (sum-squares (+ a 1) b))))
sum-squares

(sum-squares 1 5) ;;高次手続きでない
55

(defun sum (term a b)
  (if (> a b)
      0
    (+ (funcall term a)
       (sum term (+ a 1) b))))
sum
(defun square(a) (* a a))
square
(defun sum-squares (a b)
  (sum 'square a b))
sum-squares 
(sum-squares 1 5) ;;高次手続き
55
