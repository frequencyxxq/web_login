from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organization(models.Model):
    """
    Organization table.
    """

    name = models.CharField(
        max_length=255, verbose_name="组织名称", blank=False, default=None
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Organization"


class Room(models.Model):
    """
    Room table.
    """

    number = models.CharField(
        max_length=20, verbose_name="房间号", blank=False, default=None
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "Room"


class IssueCategory(models.Model):
    """
    Issue category (问题大分类).
    """

    content = models.CharField(
        max_length=255, verbose_name="内容", blank=False, default=None
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Issue category"


class IssueSubcategory(models.Model):
    """
    Issue subcategory (问题子类).
    """

    content = models.CharField(
        max_length=255, verbose_name="内容", blank=False, default=None
    )
    issue_categoty = models.ForeignKey(IssueCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Issue subcategory"


TICKET_CHOICES = (
    ("PENDING", "Pending"),
    ("COMPLETED", "Completed"),
)


class Ticket(models.Model):
    # 注册的用户会有这个信息
    user = models.ForeignKey(User, related_name="ticket", on_delete=models.PROTECT)

    reporter = models.CharField(
        max_length=100, verbose_name="报修人", blank=False, default=None
    )
    solved_by = models.CharField(
        max_length=100, verbose_name="处理人", default=None, blank=True
    )
    mobile_phone = models.CharField(
        max_length=20, verbose_name="手机号", blank=False, default=None
    )
    remark = models.TextField(verbose_name="问题描述", blank=False, default=None)
    status = models.CharField(
        max_length=15,
        choices=TICKET_CHOICES,
        default="PENDING",
        verbose_name="工单状态",
    )
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    issue_category = models.ForeignKey(IssueCategory, on_delete=models.CASCADE)
    issue_subcategory = models.ForeignKey(IssueSubcategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
