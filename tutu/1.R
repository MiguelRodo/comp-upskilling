library(tibble)
participants <- data.frame(
  id = LETTERS[1:6],
  received_injection = c(TRUE, TRUE, TRUE, TRUE, TRUE, FALSE),
  hiv_negative_day0 = c(TRUE, TRUE, TRUE, TRUE, FALSE, TRUE),
  diagnosis_month = c(10, NA, NA, 27, 0, NA),
  last_negative_month = c(9, 14, 24, 24, NA, 0)
) |>
  tibble::as_tibble()

# c1
p_c1 <- participants |>
  dplyr::filter(hiv_negative_day0 & received_injection)

# c2
p_c2 <- purrr::map_df(unique(p_c1$id), function(id) {
  row_curr <- p_c1 |> dplyr::filter(.data$id == .env$id)
  month_last_neg <- row_curr$last_negative_month
  month_diag <- row_curr$diagnosis_month
  event_lgl <- (!is.na(month_diag)) & month_diag <= 24
  time <- if (event_lgl) month_diag else min(24, month_last_neg)
  tibble::tibble(
    id = row_curr$id,
    time = time,
    event = as.integer(event_lgl)
  ) 
})

# c3
p_c3 <- p_c2 |>
  dplyr::left_join(
    participants,
    by = c("id")
  )
for (i in seq_len(nrow(p_c3))) {
  row_curr <- p_c3[i, ]
  id <- row_curr[["id"]]
  time <- row_curr[["time"]]
  event <- row_curr[["event"]]
  month_diag <- row_curr[["diagnosis_month"]]
  month_last_neg <- row_curr[["last_negative_month"]]
  if (event == 1) {
    stopifnot((!is.na(month_diag)) && month_diag <= 24)
    stopifnot(time == month_diag)
  }
}

1. Y(10) is 4, dN(10) is 1
2. 1/4, 1-exp(-0.25)
3. 0.75
4. No, only jumps at events

