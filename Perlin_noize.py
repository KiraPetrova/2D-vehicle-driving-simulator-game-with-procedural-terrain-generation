import numpy as np


def smoothstep(t):
    return t * t * (3 - 2 * t)


def perlin_noize(world_width, frequency, seed):
    rng = np.random.default_rng(seed)
    gradients = rng.random((int(world_width * frequency) + 2)) * 2 - 1

    array = np.arange(world_width)

    inf_about_all_points = array * frequency
    left_nodes = np.floor(inf_about_all_points).astype(int)
    depth_within_a_segments = inf_about_all_points - left_nodes

    a = gradients[left_nodes]
    b = gradients[left_nodes + 1]

    influence_of_the_left_nodes = a * depth_within_a_segments
    influence_of_the_right_nodes = b * (depth_within_a_segments - 1)

    a_curve = smoothstep(depth_within_a_segments)

    result = influence_of_the_left_nodes * (
            1 - a_curve) + influence_of_the_right_nodes * a_curve

    result = smoothstep(result)

    return result


def perlin_noize_octaves(world_width, frequencies, amplitudes, seeds):
    k_of_octaves = frequencies.shape[0]
    results = np.zeros((k_of_octaves, world_width))

    for i in range(k_of_octaves):
        results[i, :] = perlin_noize(world_width, frequencies[i], seeds[i]) * amplitudes[i]

    total_result = np.sum(results, axis=0)

    return total_result
