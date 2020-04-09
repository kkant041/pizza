from django.db import models

# Create your models here.


class regularpizza(models.Model):
    """Model definition for regularpizza."""

    # TODO: Define fields here
    reg_pizza = models.CharField(max_length=100)
    productID = models.PositiveIntegerField()
    reg_small_price = models.DecimalField(max_digits=10, decimal_places=2)
    reg_large_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        """Meta definition for regularpizza."""

        verbose_name = 'regularpizza'
        verbose_name_plural = 'regularpizzas'

    def __str__(self):
        """Unicode representation of regularpizza."""
        return '%s %s %s %s' % (self.reg_pizza, self.productID, self.reg_small_price, self.reg_large_price)


class sicilianpizza(models.Model):
    """Model definition for sicilianpizza."""

    # TODO: Define fields here
    sic_pizza = models.CharField(max_length=100)
    productID = models.PositiveIntegerField()
    sic_small_price = models.DecimalField(max_digits=10, decimal_places=2)
    sic_large_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        """Meta definition for sicilianpizza."""

        verbose_name = 'sicilianpizza'
        verbose_name_plural = 'sicilianpizzas'

    def __str__(self):
        """Unicode representation of sicilianpizza."""
        return '%s %s %s %s' % (self.sic_pizza, self.productID, self.sic_small_price, self.sic_large_price)


class topping(models.Model):
    """Model definition for topping."""

    # TODO: Define fields here
    top_name = models.CharField(max_length=100)

    class Meta:
        """Meta definition for topping."""

        verbose_name = 'topping'
        verbose_name_plural = 'toppings'

    def __str__(self):
        """Unicode representation of topping."""
        return (self.top_name)


class sub(models.Model):
    """Model definition for sub."""

    # TODO: Define fields here
    sub_name = models.CharField(max_length=100)
    productID = models.PositiveIntegerField()
    sub_small_price = models.DecimalField(max_digits=10, decimal_places=2)
    sub_large_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        """Meta definition for sub."""

        verbose_name = 'sub'
        verbose_name_plural = 'subs'

    def __str__(self):
        """Unicode representation of sub."""
        return '%s %s %s %s' % (self.sub_name, self.productID, self.sub_small_price, self.sub_large_price)


class pasta(models.Model):
    """Model definition for pasta."""

    # TODO: Define fields here
    pasta_name = models.CharField(max_length=100)
    productID = models.PositiveIntegerField()
    pasta_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        """Meta definition for pasta."""

        verbose_name = 'pasta'
        verbose_name_plural = 'pasta'

    def __str__(self):
        """Unicode representation of pasta."""
        return '%s %s %s' % (self.pasta_name, self.productID, self.pasta_price)


class salad(models.Model):
    """Model definition for salad."""

    # TODO: Define fields here
    salad_name = models.CharField(max_length=100)
    productID = models.PositiveIntegerField()
    salad_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        """Meta definition for salad."""

        verbose_name = 'salad'
        verbose_name_plural = 'salad'

    def __str__(self):
        """Unicode representation of salad."""
        return '%s %s %s' % (self.salad_name, self.productID, self.salad_price)


class dinner_platter(models.Model):
    """Model definition for dinner_platter."""

    # TODO: Define fields here
    platter_name = models.CharField(max_length=100)
    productID = models.PositiveIntegerField()
    platter_small_price = models.DecimalField(max_digits=10, decimal_places=2)
    platter_large_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        """Meta definition for dinner_platter."""

        verbose_name = 'dinner_platter'
        verbose_name_plural = 'dinner_platters'

    def __str__(self):
        """Unicode representation of dinner_platter."""
        return '%s %s %s %s' % (self.platter_name, self.productID, self.platter_small_price, self.platter_large_price)


class cartItems(models.Model):
    """Model definition for cartItems."""

    # TODO: Define fields here
    username = models.CharField(max_length=100)
    productID = models.PositiveIntegerField(default=0)
    productType = models.CharField(max_length=100)
    numOfProducts = models.PositiveIntegerField(default=0)

    class Meta:
        """Meta definition for cartItems."""

        verbose_name = 'cartItems'
        verbose_name_plural = 'cartItems'

    def __str__(self):
        """Unicode representation of cartItems."""
        return '%s %s %s %i' % (self.username, self.productID, self.productType, self.numOfProducts)
