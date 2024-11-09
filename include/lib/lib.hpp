#pragma once

/**
 * @brief Computes the inverse square root of a given number.
 * 
 * This function uses a fast approximation algorithm to compute the inverse square root
 * of a floating-point number. It is commonly used in graphics and game development
 * for its performance benefits.
 * 
 * @param number The floating-point number for which to compute the inverse square root.
 * @return The inverse square root of the given number.
 */
float Q_rsqrt( float number );
