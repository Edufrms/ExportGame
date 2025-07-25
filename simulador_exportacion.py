import streamlit as st

st.set_page_config(page_title="Simulador de Exportación", layout="centered")

st.title("🧀 Simulador de Exportación: Queso a Canadá")

st.markdown("Simula una operación real de exportación de queso desde España hacia Canadá. Calcularemos el beneficio o pérdida neta teniendo en cuenta aranceles, logística y licencias.")

# Parámetros fijos
precio_compra = 2000  # €/tonelada
precio_venta_cad = 3200  # CAD/tonelada
tipo_cambio = 1.45  # 1 EUR = 1.45 CAD
arancel = 0.20  # 20%
logistica = 400  # €
licencia = 200  # €

# Input del usuario
cantidad_tn = st.number_input("📦 Cantidad a exportar (en toneladas)", min_value=0.1, step=0.1)

if cantidad_tn:
    st.markdown("## 📊 Resultados")

    # Cálculos
    ingreso_total_cad = cantidad_tn * precio_venta_cad
    ingreso_total_eur = ingreso_total_cad / tipo_cambio

    arancel_total = ingreso_total_eur * arancel
    coste_total = (precio_compra * cantidad_tn) + logistica + licencia + arancel_total
    beneficio = ingreso_total_eur - coste_total

    # Mostrar resultados
    st.write(f"🔹 Ingreso total en CAD: {ingreso_total_cad:,.2f} CAD")
    st.write(f"🔹 Ingreso total en EUR: {ingreso_total_eur:,.2f} €")
    st.write(f"🔸 Coste arancelario: {arancel_total:,.2f} €")
    st.write(f"🔸 Coste total (producto + logística + licencia + arancel): {coste_total:,.2f} €")
    st.write(f"💰 **Beneficio neto**: {'+' if beneficio >= 0 else ''}{beneficio:,.2f} €")

    if beneficio >= 0:
        st.success("¡Exportación rentable!")
    else:
        st.error("La operación genera pérdidas.")
