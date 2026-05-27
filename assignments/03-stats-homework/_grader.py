"""Hidden grader for HW4.

Students see PASS / FAIL only. Expected values are stored as SHA256 hashes
of rounded numeric values. Floats with tolerance are snapped to a rounding
grid before hashing, so a student answer within tolerance hashes to the
same digest.
"""
import hashlib

# tolerance per task ID: the value the student submits is rounded to this many
# decimals before hashing. Pick tolerance ≈ half the rounding step.
_TOLERANCE = {
    "1a_mean_emp": 3,        # Bernoulli sample mean to 3 decimals → ±0.0005
    "1a_var_emp": 3,
    "1b_mean_emp": 2,        # Normal sample mean to 2 decimals → ±0.005
    "1b_std_emp": 2,
    "1c_ecdf_at_0": 2,       # ECDF value at x=0 → ±0.005
    "2_n": 0,
    "2_mean": 2,
    "2_median": 2,
    "2_std": 2,
    "2_iqr": 2,
    "2_ci_low": 2,
    "2_ci_high": 2,
    "3_z_manual": 2,         # Z-statistic for one-sample
    "3_p_z": 3,
    "3_p_t": 3,
    "3_decision": 0,         # 0 = fail to reject, 1 = reject
    "4_z_stat": 2,
    "4_z_p": 3,
    "4_perm_p": 2,           # permutation p-value ±0.005 (varies with sim)
    "4_decision": 0,
    "5a_fpr": 2,             # empirical FPR ≈ 0.05 ± 0.01
    "5b_tpr": 2,             # empirical power
    "5c_fpr_broken": 2,      # empirical FPR with broken assumption
    "6a_ci_low": 2,
    "6a_ci_high": 2,
    "6c_median_ci_low": 2,
    "6c_median_ci_high": 2,
}

# Pre-computed answer hashes (SHA256 of "task_id|rounded_value").
# Generated from the canonical solution against the fixed-seed dataset.
_HASHES = {
    "1a_mean_emp": "ec913c59d3952b373e886a4a9deb06dffa8ee925df30df8acd5cf93b861b9dc6",
    "1a_var_emp": "7b468ea0e742f72d25bcf226c0c3ecc440146262e5be4038aea14a3f924d3572",
    "1b_mean_emp": "fd72bc48c22cad0d033794a5675f09db06c0ca336ebd6d8b6ef4e710f52658df",
    "1b_std_emp": "ca2f6efc71dbd9964234588f46bea2bd88ed07c9bb94ed71a967242dd197aa35",
    "1c_ecdf_at_0": "85e23f446f5b08e3f0573f1114616047b74b3286877dab8ea0e1063059bd6cf7",
    "2_n": "45b6898af2f5fed6ea1cb6d2119d8d5e2ef2d371714bedf82562a8621badee70",
    "2_mean": "b004da3bcc2aa653c2adc06035ed8d9bafc05d35884579599cf685389db55f3e",
    "2_median": "acf8245926844eb414f123092e77baf1c7b63f802130567ea796816ac9435b1b",
    "2_std": "046b5b3d5e35290c2a6fcf791ebbeada23f02f6daebb57a1971b67e4e6f231fc",
    "2_iqr": "9e3dcddb08c8f0e654e41075d861ad964a6b4ad08b30c588f757ea444b7fc4aa",
    "2_ci_low": "34460ca466bcffe07efc283f6efbb2cacca11b26ba9f859ced92bfeda0dca436",
    "2_ci_high": "9a4687d21365d2ec21704ab7d3ce22e2e82736bb450430a6f045c9b1063e6ea7",
    "3_z_manual": "eae258a5e2b4525b096d8328932f8d6b712a19bac651d3e56758b55680e7d213",
    "3_p_z": "7f12dec224213ae8cff6abd272736c46c68f88f3f9f643229584a56790e5f34f",
    "3_p_t": "835930b69907857391c811107e71525c9623ae1675b0dce4f3626902bfc94537",
    "3_decision": "41468a123fa080049075483aafdfe340350b59f19e664b2b4abc5b5db66fc6ea",
    "4_z_stat": "af866c4f9bca10a51896bd35285e147e11ef5d82fa6d409e78989e8317b1296a",
    "4_z_p": "d340f7f2ec5c56e7a6379752f68d2646ce9c7a3bb0ae1bd54d0786b148928b14",
    "4_perm_p": "87bb15f28bcc40866e21178f41ac23ae8867cafefba6e3dade20824288e4bce4",
    "4_decision": "0cafbfe33592c7970cd4c660047745de45639a359ddc2ae9ec9854b35cce8d77",
    "5a_fpr": "78b2104b56c758a5740eeaa5d33067676ce3ed61ae48cdad78b2427c767f83b5",
    "5b_tpr": "a432f09e4552ee0527131956db22349028624ce8d59403ead25bab42bdffb19e",
    "5c_fpr_broken": "971cc01fa1c9a3c424c042ea3ff810f713430d6f814efc80e3797a8a5ec8de15",
    "6a_ci_low": "bfa285fd5f1b66f303d7a63d0299876b651dcf8ba9b6bd6ee36169fded38ceb0",
    "6a_ci_high": "30e1b656f11aae5db7889ea87bd57a1d8ee9002ce895dac88fd107787e75116e",
    "6c_median_ci_low": "fe53bbafd26a25b480e6efc100aaca371861bd572f1b0b4ae4817484014c878e",
    "6c_median_ci_high": "a981e97d3db41e60542fea1f97f419c0b89b40fb22809695521de0a9644b8c32",
}


def _hash(task_id: str, value) -> str:
    tol = _TOLERANCE[task_id]
    rounded = round(float(value), tol)
    # Normalize -0.0 → 0.0
    if rounded == 0.0:
        rounded = 0.0
    key = f"{task_id}|{rounded:.{tol}f}"
    return hashlib.sha256(key.encode()).hexdigest()


def check_answer(task_id: str, value) -> str:
    """Compare student value to the stored answer hash. Print PASS / FAIL."""
    if task_id not in _HASHES:
        msg = f"FAIL: unknown task '{task_id}'"
        print(msg)
        return msg
    if _HASHES[task_id] == "PLACEHOLDER":
        msg = f"WARN task {task_id}: grader not yet populated (instructor side)"
        print(msg)
        return msg
    expected = _HASHES[task_id]
    actual = _hash(task_id, value)
    if expected == actual:
        msg = f"PASS task {task_id}"
    else:
        tol = _TOLERANCE[task_id]
        msg = f"FAIL task {task_id}: got {round(float(value), tol)} — does not match expected"
    print(msg)
    return msg
