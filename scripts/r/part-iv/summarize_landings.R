#!/usr/bin/env Rscript

# Valida y resume el caso sintético usando únicamente R base.
args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 2L) {
  stop("Uso: Rscript summarize_landings.R <entrada.csv> <salida.csv>")
}

required <- c("date", "port", "fleet", "species", "landings_t", "source_id", "quality_flag")
input <- read.csv(args[[1]], stringsAsFactors = FALSE, check.names = FALSE)

if (!setequal(names(input), required)) stop("El esquema de columnas no coincide")
if (anyDuplicated(input$source_id)) stop("source_id contiene duplicados")
if (any(is.na(as.Date(input$date)))) stop("date contiene valores inválidos")
numeric_landings <- suppressWarnings(as.numeric(input$landings_t))
if (any(is.na(numeric_landings))) stop("landings_t contiene valores no numéricos")
input$landings_t <- numeric_landings
if (any(!input$quality_flag %in% c("ok", "review", "invalid"))) stop("quality_flag desconocido")
if (any(input$landings_t < 0 & input$quality_flag != "invalid")) {
  stop("Un valor negativo carece de la marca invalid")
}

valid <- input[input$quality_flag != "invalid", ]
summary <- aggregate(landings_t ~ species, data = valid, FUN = sum)
summary <- summary[order(summary$species), ]
dir.create(dirname(args[[2]]), recursive = TRUE, showWarnings = FALSE)
write.csv(summary, args[[2]], row.names = FALSE, quote = FALSE)
message(
  sprintf(
    "Validación superada: %d registros leídos, %d excluidos y %d especies resumidas.",
    nrow(input), sum(input$quality_flag == "invalid"), nrow(summary)
  )
)
message(sprintf("Salida escrita: %s", args[[2]]))
