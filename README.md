# README

The purpose of this project is to
`[briefly describe the project's goals and objectives]`

## Reproducing the analysis

Run the following code from the project working directory:

Clone the repository:

    git clone https://github.com/MiguelRodo/comp-upskilling -b tutu-competency-assessment tutu

Switch to the project directory, e.g.:

    cd tutu

Restore the R packages and their versions:

    renv::restore()

    ## - The library is already synchronized with the lockfile.

In `R`, restore the raw data:

    projr::projr_restore()

    ## ℹ Checking raw-docs, raw-data against build v0.6.0

    ## ✔ Verified raw-docs, raw-data for build v0.6.0

Run the build:

    projr::projr_build_dev()

    ## 

    ## ── Development Build: Pre-Build Preparation ──────────────────────────────────────────────────────────────────────────────────────────────────────

    ## • Checking project configuration

    ## • Setting build version to 0.6.0-1

    ## 

    ## ── Development Build: Build ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

    ## • Rendering Quarto document 01-data-prep.qmd

    ## [31m
    ## 
    ## processing file: 01-data-prep.qmd
    ## [39m1/74                   
    ## 2/74 [unnamed-chunk-1] 
    ## 3/74                   
    ## 4/74 [unnamed-chunk-2] 
    ## 5/74                   
    ## 6/74 [unnamed-chunk-3] 
    ## 7/74                   
    ## 8/74 [unnamed-chunk-4] 
    ## 9/74                   
    ## 10/74 [unnamed-chunk-5] 
    ## 11/74                   
    ## 12/74 [unnamed-chunk-6] 
    ## 13/74                   
    ## 14/74 [unnamed-chunk-7] 
    ## 15/74                   
    ## 16/74 [unnamed-chunk-8] 
    ## 17/74                   
    ## 18/74 [unnamed-chunk-9] 
    ## 19/74                   
    ## 20/74 [unnamed-chunk-10]
    ## 21/74                   
    ## 22/74 [unnamed-chunk-11]
    ## 23/74                   
    ## 24/74 [unnamed-chunk-12]
    ## 25/74                   
    ## 26/74 [unnamed-chunk-13]
    ## 27/74                   
    ## 28/74 [unnamed-chunk-14]
    ## 29/74                   
    ## 30/74 [unnamed-chunk-15]
    ## 31/74                   
    ## 32/74 [unnamed-chunk-16]
    ## 33/74                   
    ## 34/74 [unnamed-chunk-17]
    ## 35/74                   
    ## 36/74 [unnamed-chunk-18]
    ## 37/74                   
    ## 38/74 [unnamed-chunk-19]
    ## 39/74                   
    ## 40/74 [unnamed-chunk-20]
    ## 41/74                   
    ## 42/74 [unnamed-chunk-21]
    ## 43/74                   
    ## 44/74 [unnamed-chunk-22]
    ## 45/74                   
    ## 46/74 [unnamed-chunk-23]
    ## 47/74                   
    ## 48/74 [unnamed-chunk-24]
    ## 49/74                   
    ## 50/74 [unnamed-chunk-25]
    ## 51/74                   
    ## 52/74 [unnamed-chunk-26]
    ## 53/74                   
    ## 54/74 [unnamed-chunk-27]
    ## 55/74                   
    ## 56/74 [unnamed-chunk-28]
    ## 57/74                   
    ## 58/74 [unnamed-chunk-29]
    ## 59/74                   
    ## 60/74 [unnamed-chunk-30]
    ## 61/74                   
    ## 62/74 [unnamed-chunk-31]
    ## 63/74                   
    ## 64/74 [unnamed-chunk-32]
    ## 65/74                   
    ## 66/74 [unnamed-chunk-33]
    ## 67/74                   
    ## 68/74 [unnamed-chunk-34]
    ## 69/74                   
    ## 70/74 [unnamed-chunk-35]
    ## 71/74                   
    ## 72/74 [unnamed-chunk-36]
    ## 73/74                   
    ## 74/74 [unnamed-chunk-37]
    ## [31moutput file: 01-data-prep.knit.md
    ## 
    ## [39m[1mpandoc [22m
    ##   to: html
    ##   output-file: 01-data-prep.html
    ##   standalone: true
    ##   embed-resources: true
    ##   section-divs: true
    ##   html-math-method: mathjax
    ##   wrap: none
    ##   default-image-extension: png
    ##   
    ## [1mmetadata[22m
    ##   document-css: false
    ##   link-citations: true
    ##   date-format: long
    ##   lang: en
    ##   title: 'Task 2: Data Preparation'
    ##   
    ## Output created: 01-data-prep.html

    ## • Rendering Quarto document 02-primary-analysis.qmd

    ## [31m
    ## 
    ## processing file: 02-primary-analysis.qmd
    ## [39m1/21                   
    ## 2/21 [unnamed-chunk-1] 
    ## 3/21                   
    ## 4/21 [unnamed-chunk-2] 
    ## 5/21                   
    ## 6/21 [unnamed-chunk-3] 
    ## 7/21                   
    ## 8/21 [unnamed-chunk-4] 
    ## 9/21                   
    ## 10/21 [unnamed-chunk-5] 
    ## 11/21                   
    ## 12/21 [unnamed-chunk-6] 
    ## 13/21                   
    ## 14/21 [unnamed-chunk-7] 
    ## 15/21                   
    ## 16/21 [unnamed-chunk-8] 
    ## 17/21                   
    ## 18/21 [unnamed-chunk-9] 
    ## 19/21                   
    ## 20/21 [unnamed-chunk-10]
    ## 21/21                   
    ## [31moutput file: 02-primary-analysis.knit.md
    ## 
    ## [39m[1mpandoc [22m
    ##   to: html
    ##   output-file: 02-primary-analysis.html
    ##   standalone: true
    ##   embed-resources: true
    ##   section-divs: true
    ##   html-math-method: mathjax
    ##   wrap: none
    ##   default-image-extension: png
    ##   
    ## [1mmetadata[22m
    ##   document-css: false
    ##   link-citations: true
    ##   date-format: long
    ##   lang: en
    ##   title: 'Task 2: Primary Analysis'
    ##   
    ## Output created: 02-primary-analysis.html

    ## • Rendering Quarto document 04-clinical-summary.qmd

    ## [1mpandoc [22m
    ##   to: latex
    ##   output-file: 04-clinical-summary.tex
    ##   standalone: true
    ##   embed-resources: true
    ##   pdf-engine: lualatex
    ##   variables:
    ##     graphics: true
    ##     tables: true
    ##   default-image-extension: pdf
    ##   
    ## [1mmetadata[22m
    ##   documentclass: scrartcl
    ##   classoption:
    ##     - DIV=11
    ##     - numbers=noendperiod
    ##   papersize: letter
    ##   header-includes:
    ##     - \KOMAoption{captions}{tableheading}
    ##   block-headings: true
    ##   title: 'Task 4: Clinical Summary'
    ##   
    ## [1m[34m
    ## Rendering PDF[39m[22m
    ## [1m[34mrunning lualatex - 1[39m[22m
    ##   This is LuaHBTeX, Version 1.24.0 (TeX Live 2026) 
    ##    restricted system commands enabled.
    ##   
    ## [1m[34mrunning lualatex - 2[39m[22m
    ##   This is LuaHBTeX, Version 1.24.0 (TeX Live 2026) 
    ##    restricted system commands enabled.
    ##   
    ## 
    ## Output created: 04-clinical-summary.pdf

    ## 

    ## ── Development Build: Post-Build ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────

    ## ℹ Collected 3 rendered documents in _tmp/projr/v0.6.0-1/docs

    ## ✔ Build completed successfully

The outputs will be under `_tmp/projr/v<version>/` (initially,
`v<version>` will be `v<0.3.0-1>`) with `data` and `docs` as the
sub-folders containing processed data and rendered documents.

## Installing the package

    if (!requireNamespace("remotes", quietly = TRUE)) {
      install.packages("remotes")
    }
    remotes::install_github("MiguelRodo/comp-upskilling@tutu-competency-assessment")

The processed data can then be loaded a follows:

    data("data_merged_tidy", "data_surv_tidy", package = "tutuCompetency")

## Directory Structure

This project follows a structured directory layout to organise input
materials, generated outputs, and temporary files efficiently:

- **`_reference/`**: Static documents that are not generated by
  analyses, such as assignment questions and reference materials.
- **`_raw_data/`**: Raw, unprocessed data files.
- **`docs/`**: Rendered documents produced from R Markdown (`Rmd`) or
  Quarto (`qmd`) scripts.
- **`_output/`**: Final analysis results, processed data, and exported
  reports.
- **`_tmp/`**: Temporary storage for cached outputs, intermediate
  results, and shared files.

## Change Log

Summary of updates is included below. For more detailed run information,
including scripts run and configurations used, see
[BUILDLOG.md](BUILDLOG.md).

# CHANGELOG

- *Minor* (v0.6.0): Miguel Rodo (2026-11-23 11:46:14)
  - Add tasks 2 and 4
- *Minor* (v0.5.0): Miguel Rodo (2026-11-23 11:41:10)
  - Build tasks 2 and 4
- *Minor* (v0.3.0): Miguel Rodo (2026-11-23 11:36:04)
  - Add tasks 2 and 4
- *Minor* (v0.2.0): Miguel Rodo (2026-11-23 11:05:31)
  - Add primary analysis and clinical summary
- *Minor* (v0.1.0): Miguel Rodo (2026-11-23 10:30:34)
  - Add processed data
- Patch (v0.0.2): Miguel Rodo (2026-11-23 07:38:39)
  - Tste
