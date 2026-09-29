use rust_challenges::challenges::challenge_2::*;

#[test]
fn test_calculate_area() {
    let area = calculate_area();

    assert!(
        area > 0,
        "The `calculate_area` function must return a value greater than 0"
    );
}

#[test]
fn test_prints_values_runs() {
    prints_values(10, 50);
}