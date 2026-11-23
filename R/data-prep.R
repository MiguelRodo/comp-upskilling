audit_table <- function(data, show_rows = TRUE, ...) {
  if (show_rows) {
    print(data, ...)
  }
  print(tibble::tibble(
    n_rows = nrow(data),
    n_participants = dplyr::n_distinct(data$subjid, na.rm = TRUE)
  ))
  invisible(data)
}
