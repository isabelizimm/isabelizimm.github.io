library(tidymodels)
data(Chicago)

chicago_small <- Chicago %>% slice(1:730) # two years of data

chicago_rec <-
  recipe(ridership ~ ., data = Chicago) %>%
  step_date(date) %>%
  step_holiday(date, keep_original_cols = FALSE) %>%
  step_dummy(all_nominal_predictors()) %>%
  step_zv(all_predictors()) %>%
  step_normalize(all_predictors()) %>%
  step_pca(all_of(stations), num_comp = 4)


tree_model <-
  svm_linear() %>%
  set_engine("LiblineaR") %>%
  set_mode("regression")

home_game_model <-
  workflow(chicago_rec, tree_model) %>%
  fit(chicago_small)


linear_model <-
  linear_reg() %>%
  set_engine("lm")

not_home_game_model <-
  workflow(chicago_rec, tree_model) %>%
  fit(chicago_small)


library(vetiver)

home <- vetiver_model(home_game_model, "home")
not_home <- vetiver_model(not_home_game_model, "not_home")

library(plumber)

pr() %>%
  vetiver_pr_post(home, path = "/home_game") %>%
  vetiver_pr_docs(home) %>%
  vetiver_pr_post(not_home, path = "/not_home_game") %>%
  vetiver_pr_docs(not_home) %>%
  pr_run()
