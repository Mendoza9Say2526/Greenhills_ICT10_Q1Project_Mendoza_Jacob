# Reciept Generator Calculation
from pyscript import display, document


def place_order(e):
        document.getElementById('show').innerHTML = " "
        prod1 = document.getElementById('item1')
        prod2 = document.getElementById('item2')
        prod3 = document.getElementById('item3')
        prod4 = document.getElementById('item4')
        prod5 = document.getElementById('item5')

        name1 = "Bruschetta"
        name2 = "Pizza"
        name3 = "Tiramisu"
        name4 = "Red Wine"
        name5 = "Spaghetti Bolognese"

        subtotal = float(prod1.value) * prod1.checked + float(prod2.value) * prod2.checked + float(prod3.value) * prod3.checked + float(prod4.value) * prod4.checked + float(prod5.value) * prod5.checked

        vat_rate = 0.12
        vat_amount = subtotal * vat_rate
        total_price = subtotal + vat_amount

        display(f"Subtotal: ₱{subtotal}", target="show")
        display(f"Vat: ₱{vat_amount}", target="show")
        display(f"Total Amount: ₱{total_price}", target="show")

# Generating SKU
def gen_sku(e):
        categ = document.getElementById("cat").value
        prod = document.getElementById("prod").value
        stock = document.getElementById("stock").value
        product_code = prod.strip().lower()[0:3]
        sku = categ + product_code + stock
        display(sku, target="sku-result")

# sku and reciept pages that are switching
def present_sku(e):
    document.getElementById("receipt-page").hidden = True
    document.getElementById("sku-page").hidden = False

def present_receipt(e):
    document.getElementById("sku-page").hidden = True
    document.getElementById("receipt-page").hidden = False

















