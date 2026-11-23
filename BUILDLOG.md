# BUILDLOG

### v0.5.0: Miguel Rodo (2026-11-23 11:41:10)

**Description**

Build tasks 2 and 4

**Metadata**

- Total time: 
2min 5s
- `projr` profile: 
default

**Inputs Changes (v0.3.0 -> v0.5.0)**

- `raw-data`: No changes (4 file(s) unchanged)
- No changes detected in inputs

**Outputs Changes (v0.3.0 -> v0.5.0)**

- `docs`:
  - 3 modified
  - Modified: 01-data-prep.html, 02-primary-analysis.html, 04-clinical-summary.pdf

**System Resources**

- OS: Linux 6.8.0-1070-azure
- OS Version: #78~22.04.1-Ubuntu SMP Thu Sep 24 18:46:45 UTC 2026
- Architecture: x86_64
- Platform: x86_64-pc-linux-gnu
- CPU Cores: 4
- Total RAM: 15Gi
- Disk Space: 32G total, 21G available

**`projr` config**

```yaml
directories:
  raw-docs:
    path: _reference
  raw-data:
    path: _raw_data
    source:
      github: archive
  cache:
    path: _tmp
  output:
    path: _output
  docs:
    path: docs
  data:
    path: data
build:
  scripts:
  - ''
  - 01-data-prep.qmd
  - 02-primary-analysis.qmd
  - 04-clinical-summary.qmd
  github:
    archive:
      content:
      - raw-data
      - output
      - raw-docs
      - docs
      structure: archive

```

**Session info**

```
R version 4.6.1 (2026-06-24)
Platform: x86_64-pc-linux-gnu
Running under: Ubuntu 24.04.4 LTS

Matrix products: default
BLAS:   /usr/lib/x86_64-linux-gnu/openblas-pthread/libblas.so.3 
LAPACK: /usr/lib/x86_64-linux-gnu/openblas-pthread/libopenblasp-r0.3.26.so;  LAPACK version 3.12.0

locale:
 [1] LC_CTYPE=en_US.UTF-8       LC_NUMERIC=C              
 [3] LC_TIME=en_US.UTF-8        LC_COLLATE=en_US.UTF-8    
 [5] LC_MONETARY=en_US.UTF-8    LC_MESSAGES=en_US.UTF-8   
 [7] LC_PAPER=en_US.UTF-8       LC_NAME=C                 
 [9] LC_ADDRESS=C               LC_TELEPHONE=C            
[11] LC_MEASUREMENT=en_US.UTF-8 LC_IDENTIFICATION=C       

time zone: Etc/UTC
tzcode source: system (glibc)

attached base packages:
[1] stats     graphics  grDevices datasets  utils     methods   base     

loaded via a namespace (and not attached):
 [1] vctrs_0.7.3       httr_1.4.9        cli_3.6.6         knitr_1.52       
 [5] rlang_1.3.0       xfun_0.62         processx_3.10.0   renv_1.3.1       
 [9] jsonlite_2.0.0    gitcreds_0.1.2    glue_1.8.1        rprojroot_2.1.1  
[13] htmltools_0.5.9   quarto_1.5.1      ps_1.9.3          rmarkdown_2.32   
[17] filelock_1.0.3    tibble_3.3.1      evaluate_1.0.5    ini_0.3.1        
[21] fastmap_1.2.0     yaml_2.3.12       lifecycle_1.0.5   projr_0.5.2-10   
[25] compiler_4.6.1    fs_2.1.0          pkgconfig_2.0.3   Rcpp_1.1.2       
[29] rstudioapi_0.19.0 later_1.4.8       gh_1.6.1          digest_0.6.39    
[33] R6_2.6.1          parallel_4.6.1    pillar_1.11.1     curl_8.1.0       
[37] magrittr_2.0.5    uuid_1.2-2        tools_4.6.1      
```

----

### v0.3.0: Miguel Rodo (2026-11-23 11:36:04)

**Description**

Add tasks 2 and 4

**Metadata**

- Total time: 
3min 25s
- `projr` profile: 
default

**Inputs Changes (v0.2.0 -> v0.3.0)**

- `raw-data`: No changes (4 file(s) unchanged)
- No changes detected in inputs

**Outputs Changes (v0.2.0 -> v0.3.0)**

- `docs`:
  - 3 modified
  - Modified: 01-data-prep.html, 02-primary-analysis.html, 04-clinical-summary.pdf

**System Resources**

- OS: Linux 6.8.0-1070-azure
- OS Version: #78~22.04.1-Ubuntu SMP Thu Sep 24 18:46:45 UTC 2026
- Architecture: x86_64
- Platform: x86_64-pc-linux-gnu
- CPU Cores: 4
- Total RAM: 15Gi
- Disk Space: 32G total, 21G available

**`projr` config**

```yaml
directories:
  raw-docs:
    path: _reference
  raw-data:
    path: _raw_data
    source:
      github: archive
  cache:
    path: _tmp
  output:
    path: _output
  docs:
    path: docs
  data:
    path: data
build:
  scripts:
  - ''
  - 01-data-prep.qmd
  - 02-primary-analysis.qmd
  - 04-clinical-summary.qmd
  github:
    archive:
      content:
      - raw-data
      - output
      - raw-docs
      - docs
      structure: archive

```

**Session info**

```
R version 4.6.1 (2026-06-24)
Platform: x86_64-pc-linux-gnu
Running under: Ubuntu 24.04.4 LTS

Matrix products: default
BLAS:   /usr/lib/x86_64-linux-gnu/openblas-pthread/libblas.so.3 
LAPACK: /usr/lib/x86_64-linux-gnu/openblas-pthread/libopenblasp-r0.3.26.so;  LAPACK version 3.12.0

locale:
 [1] LC_CTYPE=en_US.UTF-8       LC_NUMERIC=C              
 [3] LC_TIME=en_US.UTF-8        LC_COLLATE=en_US.UTF-8    
 [5] LC_MONETARY=en_US.UTF-8    LC_MESSAGES=en_US.UTF-8   
 [7] LC_PAPER=en_US.UTF-8       LC_NAME=C                 
 [9] LC_ADDRESS=C               LC_TELEPHONE=C            
[11] LC_MEASUREMENT=en_US.UTF-8 LC_IDENTIFICATION=C       

time zone: Etc/UTC
tzcode source: system (glibc)

attached base packages:
[1] stats     graphics  grDevices datasets  utils     methods   base     

loaded via a namespace (and not attached):
 [1] vctrs_0.7.3       httr_1.4.9        cli_3.6.6         knitr_1.52       
 [5] rlang_1.3.0       xfun_0.62         processx_3.10.0   renv_1.3.1       
 [9] jsonlite_2.0.0    gitcreds_0.1.2    glue_1.8.1        rprojroot_2.1.1  
[13] htmltools_0.5.9   quarto_1.5.1      ps_1.9.3          rmarkdown_2.32   
[17] filelock_1.0.3    tibble_3.3.1      evaluate_1.0.5    ini_0.3.1        
[21] fastmap_1.2.0     yaml_2.3.12       lifecycle_1.0.5   projr_0.5.2-10   
[25] compiler_4.6.1    fs_2.1.0          pkgconfig_2.0.3   Rcpp_1.1.2       
[29] rstudioapi_0.19.0 later_1.4.8       gh_1.6.1          digest_0.6.39    
[33] R6_2.6.1          parallel_4.6.1    pillar_1.11.1     curl_8.1.0       
[37] magrittr_2.0.5    uuid_1.2-2        tools_4.6.1      
```

----

### v0.2.0: Miguel Rodo (2026-11-23 11:05:31)

**Description**

Add primary analysis and clinical summary

**Metadata**

- Total time: 
2min 18s
- `projr` profile: 
default

**Inputs Changes (v0.1.0 -> v0.2.0)**

- `raw-data`:
  - 2 added, 2 unchanged
  - Added: processed/data_merged_tidy.rda, processed/data_surv_tidy.rda

**Outputs Changes (v0.1.0 -> v0.2.0)**

- `docs`:
  - 2 added, 1 modified
  - Added: 02-primary-analysis.html, 04-clinical-summary.pdf
  - Modified: 01-data-prep.html

**System Resources**

- OS: Linux 6.8.0-1070-azure
- OS Version: #78~22.04.1-Ubuntu SMP Thu Sep 24 18:46:45 UTC 2026
- Architecture: x86_64
- Platform: x86_64-pc-linux-gnu
- CPU Cores: 4
- Total RAM: 15Gi
- Disk Space: 32G total, 21G available

**`projr` config**

```yaml
directories:
  raw-docs:
    path: _reference
  raw-data:
    path: _raw_data
    source:
      github: archive
  cache:
    path: _tmp
  output:
    path: _output
  docs:
    path: docs
  data:
    path: data
build:
  scripts:
  - ''
  - 01-data-prep.qmd
  - 02-primary-analysis.qmd
  - 04-clinical-summary.qmd
  github:
    archive:
      content:
      - raw-data
      - output
      - raw-docs
      - docs
      structure: archive

```

**Session info**

```
R version 4.6.1 (2026-06-24)
Platform: x86_64-pc-linux-gnu
Running under: Ubuntu 24.04.4 LTS

Matrix products: default
BLAS:   /usr/lib/x86_64-linux-gnu/openblas-pthread/libblas.so.3 
LAPACK: /usr/lib/x86_64-linux-gnu/openblas-pthread/libopenblasp-r0.3.26.so;  LAPACK version 3.12.0

locale:
 [1] LC_CTYPE=en_US.UTF-8       LC_NUMERIC=C              
 [3] LC_TIME=en_US.UTF-8        LC_COLLATE=en_US.UTF-8    
 [5] LC_MONETARY=en_US.UTF-8    LC_MESSAGES=en_US.UTF-8   
 [7] LC_PAPER=en_US.UTF-8       LC_NAME=C                 
 [9] LC_ADDRESS=C               LC_TELEPHONE=C            
[11] LC_MEASUREMENT=en_US.UTF-8 LC_IDENTIFICATION=C       

time zone: Etc/UTC
tzcode source: system (glibc)

attached base packages:
[1] stats     graphics  grDevices datasets  utils     methods   base     

other attached packages:
[1] survival_3.8-12 ggplot2_4.0.4   tibble_3.3.1   

loaded via a namespace (and not attached):
 [1] Matrix_1.7-6       jsonlite_2.0.0     gtable_0.3.6       dplyr_1.2.1       
 [5] compiler_4.6.1     renv_1.3.1         filelock_1.0.3     gitcreds_0.1.2    
 [9] Rcpp_1.1.2         tidyselect_1.2.1   parallel_4.6.1     later_1.4.8       
[13] splines_4.6.1      scales_1.4.0       uuid_1.2-2         yaml_2.3.12       
[17] fastmap_1.2.0      lattice_0.22-9     R6_2.6.1           generics_0.1.4    
[21] curl_8.1.0         knitr_1.52         projr_0.5.2-10     rprojroot_2.1.1   
[25] pillar_1.11.1      RColorBrewer_1.1-3 rlang_1.3.0        UtilsDataRSV_0.1.0
[29] xfun_0.62          fs_2.1.0           S7_1.0.0           otel_0.3.0        
[33] cli_3.6.6          withr_3.0.3        magrittr_2.0.5     ps_1.9.3          
[37] gh_1.6.1           processx_3.10.0    digest_0.6.39      grid_4.6.1        
[41] rstudioapi_0.19.0  ini_0.3.1          lifecycle_1.0.5    vctrs_0.7.3       
[45] evaluate_1.0.5     glue_1.8.1         farver_2.1.2       httr_1.4.9        
[49] rmarkdown_2.32     tools_4.6.1        pkgconfig_2.0.3    quarto_1.5.1      
[53] htmltools_0.5.9   
```

----

### v0.1.0: Miguel Rodo (2026-11-23 10:30:34)

**Description**

Add processed data

**Metadata**

- Total time: 
2min 7s
- `projr` profile: 
default

**Inputs Changes (v0.0.2 -> v0.1.0)**

- `raw-data`:
  - 2 added
  - Added: baseline_cohort.csv, longitudinal_visits.csv

**Outputs Changes (v0.0.2 -> v0.1.0)**

- `docs`:
  - 1 added, 14 removed

**System Resources**

- OS: Linux 6.8.0-1070-azure
- OS Version: #78~22.04.1-Ubuntu SMP Thu Sep 24 18:46:45 UTC 2026
- Architecture: x86_64
- Platform: x86_64-pc-linux-gnu
- CPU Cores: 4
- Total RAM: 15Gi
- Disk Space: 32G total, 21G available

**`projr` config**

```yaml
directories:
  raw-docs:
    path: _reference
  raw-data:
    path: _raw_data
    source:
      github: archive
  cache:
    path: _tmp
  output:
    path: _output
  docs:
    path: docs
  data:
    path: data
build:
  scripts:
  - ''
  - 01-data-prep.qmd
  - ''
  github:
    archive:
      content:
      - raw-data
      - output
      - raw-docs
      - docs
      structure: archive

```

**Session info**

```
R version 4.6.1 (2026-06-24)
Platform: x86_64-pc-linux-gnu
Running under: Ubuntu 24.04.4 LTS

Matrix products: default
BLAS:   /usr/lib/x86_64-linux-gnu/openblas-pthread/libblas.so.3 
LAPACK: /usr/lib/x86_64-linux-gnu/openblas-pthread/libopenblasp-r0.3.26.so;  LAPACK version 3.12.0

locale:
 [1] LC_CTYPE=en_US.UTF-8       LC_NUMERIC=C              
 [3] LC_TIME=en_US.UTF-8        LC_COLLATE=en_US.UTF-8    
 [5] LC_MONETARY=en_US.UTF-8    LC_MESSAGES=en_US.UTF-8   
 [7] LC_PAPER=en_US.UTF-8       LC_NAME=C                 
 [9] LC_ADDRESS=C               LC_TELEPHONE=C            
[11] LC_MEASUREMENT=en_US.UTF-8 LC_IDENTIFICATION=C       

time zone: Etc/UTC
tzcode source: system (glibc)

attached base packages:
[1] stats     graphics  grDevices datasets  utils     methods   base     

other attached packages:
[1] tibble_3.3.1  ggplot2_4.0.4

loaded via a namespace (and not attached):
 [1] UtilsDataRSV_0.1.0 utf8_1.2.6         generics_0.1.4     projr_0.5.2-10    
 [5] renv_1.3.1         lattice_0.22-9     hms_1.1.4          digest_0.6.39     
 [9] magrittr_2.0.5     evaluate_1.0.5     grid_4.6.1         RColorBrewer_1.1-3
[13] fastmap_1.2.0      Matrix_1.7-6       rprojroot_2.1.1    jsonlite_2.0.0    
[17] processx_3.10.0    survival_3.8-12    ini_0.3.1          ps_1.9.3          
[21] httr_1.4.9         purrr_1.2.2        scales_1.4.0       cli_3.6.6         
[25] rlang_1.3.0        crayon_1.5.3       gitcreds_0.1.2     splines_4.6.1     
[29] bit64_4.8.6        withr_3.0.3        yaml_2.3.12        otel_0.3.0        
[33] tools_4.6.1        parallel_4.6.1     tzdb_0.5.0         uuid_1.2-2        
[37] dplyr_1.2.1        filelock_1.0.3     curl_8.1.0         vctrs_0.7.3       
[41] R6_2.6.1           lifecycle_1.0.5    fs_2.1.0           bit_4.6.0         
[45] vroom_1.7.1        pkgconfig_2.0.3    pillar_1.11.1      later_1.4.8       
[49] gtable_0.3.6       gh_1.6.1           glue_1.8.1         Rcpp_1.1.2        
[53] xfun_0.62          tidyselect_1.2.1   rstudioapi_0.19.0  knitr_1.52        
[57] farver_2.1.2       quarto_1.5.1       htmltools_0.5.9    rmarkdown_2.32    
[61] readr_2.2.0        compiler_4.6.1     S7_1.0.0          
```

----

#### v0.0.2: Miguel Rodo (2026-11-23 07:38:39)

**Description**

Tste

**Metadata**

- Total time: 
5s
- `projr` profile: 
default

**System Resources**

- OS: Linux 6.8.0-1070-azure
- OS Version: #78~22.04.1-Ubuntu SMP Thu Sep 24 18:46:45 UTC 2026
- Architecture: x86_64
- Platform: x86_64-pc-linux-gnu
- CPU Cores: 4
- Total RAM: 15Gi
- Disk Space: 32G total, 22G available

**`projr` config**

```yaml
directories:
  raw-docs:
    path: _reference
  raw-data:
    path: _raw_data
    source:
      github: archive
  cache:
    path: _tmp
  output:
    path: _output
  docs:
    path: docs
build:
  github:
    archive:
      content:
      - raw-data
      - output
      - raw-docs
      - docs
      structure: archive

```

**Session info**

```
R version 4.6.1 (2026-06-24)
Platform: x86_64-pc-linux-gnu
Running under: Ubuntu 24.04.4 LTS

Matrix products: default
BLAS:   /usr/lib/x86_64-linux-gnu/openblas-pthread/libblas.so.3 
LAPACK: /usr/lib/x86_64-linux-gnu/openblas-pthread/libopenblasp-r0.3.26.so;  LAPACK version 3.12.0

locale:
 [1] LC_CTYPE=en_US.UTF-8       LC_NUMERIC=C              
 [3] LC_TIME=en_US.UTF-8        LC_COLLATE=en_US.UTF-8    
 [5] LC_MONETARY=en_US.UTF-8    LC_MESSAGES=en_US.UTF-8   
 [7] LC_PAPER=en_US.UTF-8       LC_NAME=C                 
 [9] LC_ADDRESS=C               LC_TELEPHONE=C            
[11] LC_MEASUREMENT=en_US.UTF-8 LC_IDENTIFICATION=C       

time zone: Etc/UTC
tzcode source: system (glibc)

attached base packages:
[1] stats     graphics  grDevices utils     datasets  methods   base     

loaded via a namespace (and not attached):
 [1] jsonlite_2.0.0    compiler_4.6.1    renv_1.3.1        filelock_1.0.3   
 [5] gitcreds_0.1.2    Rcpp_1.1.2        parallel_4.6.1    callr_3.8.0      
 [9] later_1.4.8       uuid_1.2-2        yaml_2.3.12       fastmap_1.2.0    
[13] R6_2.6.1          pak_0.11.2        curl_7.1.0        knitr_1.52       
[17] tibble_3.3.1      projr_0.5.2-10    rprojroot_2.1.1   pillar_1.11.1    
[21] rlang_1.3.0       xfun_0.62         fs_2.1.0          otel_0.2.0       
[25] cli_3.6.6         magrittr_2.0.5    ps_1.9.3          digest_0.6.39    
[29] gh_1.6.1          processx_3.9.0    rstudioapi_0.19.0 lifecycle_1.0.5  
[33] ini_0.3.1         vctrs_0.7.3       evaluate_1.0.5    glue_1.8.1       
[37] rmarkdown_2.32    purrr_1.2.2       httr_1.4.9        tools_4.6.1      
[41] usethis_3.2.2     pkgconfig_2.0.3   quarto_1.5.1      htmltools_0.5.9  
```

----

