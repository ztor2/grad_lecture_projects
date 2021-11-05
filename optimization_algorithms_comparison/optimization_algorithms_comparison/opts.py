import numpy as np
from sympy import *
import time

###################################################################################################################

def Newton(function, init_x, tol=1e-5, max_iter=500):
    
    start = time.time()
    x_ = init_x
    x, y = symbols('x y')
    var = list(ordered(function.free_symbols))
    gradient = lambda f, var: Matrix([f]).jacobian(var)
    
    f = lambdify((x, y), function)
    f_jacobian = lambdify((x, y), gradient(function, var))
    f_hessian_inv = lambdify((x, y), hessian(function, var)**-1)
    
    f_x_new = f_jacobian(x_[0], x_[1])[0]
    
    i = 0
    while (np.linalg.norm(f_x_new) > tol) and (i < max_iter):
        hessian_inv_dot_grad = np.dot(f_hessian_inv(x_[0], x_[1]), f_jacobian(x_[0], x_[1])[0].T)
        x_ = x_ - hessian_inv_dot_grad
        f_x_new= f_jacobian(x_[0], x_[1])[0]
        i += 1
    
    elapsed = time.time() - start
    opt_x = x_
    opt_grad = np.array([np.round(f_x_new[0], 15), np.round(f_x_new[1], 15)])
    opt_func = np.round(f(opt_x[0], opt_x[1]), 15)
    
    return opt_x, opt_grad, opt_func, i, elapsed

###################################################################################################################

def BFGS(function, init_x, tol=1e-5, max_iter=500, alpha=1e-3):
    
    start = time.time()
    x_ = init_x
    x, y = symbols('x y')
    var = list(ordered(function.free_symbols))
    gradient = lambda f, var: Matrix([f]).jacobian(var)
    
    f = lambdify((x, y), function)
    f_jacobian = lambdify((x, y), gradient(function, var))
    
    min_curvature = 0.2
    f_grad = f_jacobian(x_[0], x_[1])[0]
    B = np.eye(2)
    
    curvature_violated = 0
    singular_matrix_occured = 0
    
    i = 0
    while (np.linalg.norm(f_grad) > tol) and (i < max_iter):
        
        p_k = np.linalg.solve(B, -f_grad)
        
        s_k = alpha * p_k
        x_new = x_ + alpha * p_k
        
        f_grad_new = f_jacobian(x_new[0], x_new[1])[0]    
        y_k = f_grad_new - f_grad

        if np.dot(s_k.T, y_k) <= min_curvature * np.dot(np.dot(s_k.T, B), s_k):
            update_factor = (1 - min_curvature) / (1 - np.dot(s_k.T, y_k) / np.dot(np.dot(s_k.T, B), s_k))
            y_k = update_factor * y_k + (1 - update_factor) * np.dot(B, s_k)
            curvature_violated += 1

        B_new = B + np.dot(y_k, y_k.T) / np.dot(y_k.T, s_k) - np.dot(np.dot(B, s_k), np.dot(B, s_k).T) / np.dot(s_k.T, np.dot(B, s_k))
        if np.linalg.det(B_new) != 0:
            B = B_new
        else:
            singular_matrix_occured += 1
        f_grad = f_grad_new
        x_ = x_new
        i += 1
    
    elapsed = time.time() - start
    opt_x = x_
    opt_grad = f_jacobian(opt_x[0], opt_x[1])[0]
    opt_func = f(opt_x[0], opt_x[1])

    return opt_x, opt_grad, opt_func, i, elapsed, curvature_violated, singular_matrix_occured

###################################################################################################################

def SR1(function, init_x, tol=1e-5, max_iter=500, alpha=1e-3):
    
    start = time.time()
    x_ = init_x
    x, y = symbols('x y')
    var = list(ordered(function.free_symbols))
    gradient = lambda f, var: Matrix([f]).jacobian(var)
    
    f = lambdify((x, y), function)
    f_jacobian = lambdify((x, y), gradient(function, var))
    
    min_curvature = 0.2
    f_grad = f_jacobian(x_[0], x_[1])[0]
    B = np.eye(2)
    
    singular_matrix_occured = 0
    
    i = 0
    while (np.linalg.norm(f_grad) > tol) and (i < max_iter):
        
        p_k = np.linalg.solve(B, -f_grad)
        
        s_k = alpha * p_k
        x_new = x_ + alpha * p_k
        
        f_grad_new = f_jacobian(x_new[0], x_new[1])[0]    
        y_k = f_grad_new - f_grad
            
        y_min_Bs = y_k - np.dot(B, s_k)
        B_new = B + np.dot(y_min_Bs, y_min_Bs.T) / np.dot(y_min_Bs.T, s_k)
        if np.linalg.det(B_new) != 0:
            B = B_new
        else:
            singular_matrix_occured += 1
        f_grad = f_grad_new
        x_ = x_new
        i += 1
    
    elapsed = time.time() - start
    opt_x = x_
    opt_grad = f_jacobian(opt_x[0], opt_x[1])[0]
    opt_func = f(opt_x[0], opt_x[1])

    return opt_x, opt_grad, opt_func, i, elapsed, singular_matrix_occured

###################################################################################################################