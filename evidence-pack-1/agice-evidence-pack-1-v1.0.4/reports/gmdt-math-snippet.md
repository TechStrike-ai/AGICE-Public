# GMDT (-i) Math Implementation Snippet

Algorithm-1 mapping in code:

```python
# agice/projections.py
def compute_alignment(u_disp, v):
    nu = vec_norm(u_disp)
    nv = vec_norm(v)
    if nu < _EPS or nv < _EPS:
        return 0.0
    return vec_dot(u_disp, v) / (nu * nv)

def apply_j_operator(u_disp, v_disp):
    # J[u;v] = [v; -u]
    return (list(v_disp), [-x for x in u_disp])

# in build_rotation_analysis(...):
v_disp = [v_t[i] - c_v[i] for i in range(d)]
rho = compute_alignment(u_disp, align_vec)
should_rotate = (rho < -tau) or (allow_degenerate_rotation and u_degenerate and has_history)
if should_rotate:
    w_u_rot, w_v_rot = apply_j_operator(u_disp, axis_vec)
    hints["minus_i"] = make_hint_data(..., w_u_rot, w_v_rot, tag="minus_i")
```

Runtime branching and budget split in A3:

```python
# agice/orchestrator.py
rotation_result = build_rotation_analysis(...)
projections = list(rotation_result["hints"].keys())  # base + optional minus_i
projection_sample_plan["base"] = total_candidate_budget - target_non_base
projection_sample_plan["minus_i"] += target_non_base
assert minus_i_samples >= 1, "A3 rotation applied but minus_i got 0 samples"
```

This is the concrete implementation of the geometric J-rotation branch used in A3.
