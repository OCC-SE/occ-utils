# Host environment endpoints
host = 'https://ccadmin-{env}.oracleoutsourcing.com'
app_key = 'username={user}&password={pwd}'
mfa_app_key = 'username={user}&password={pwd}&totp_code=123456'

#Admin users
admin_profiles_url = "{root_url}/ccadminui/v1/adminProfiles"

# Server side extension endpoints
server_extensions_url = "{root_url}/ccadminui/v1/serverExtensions"

# Admin UI Login endpoints
oauth_logout_admin_url = "{root_url}/ccadminui/v1/logout"
oauth_login_admin_url = "{root_url}/ccadminui/v1/login"
oauth_login_mfa_admin_url = "{root_url}/ccadminui/v1/mfalogin"

# Server side extension logging endpoints
extension_logs_url = "{root_url}/ccadminx/custom/v1/logs"

# Server side extension test endpoints
extension_tests_run_url = "{root_url}/ccadminx/custom/v1/{extensionName}/test"
extension_tests_list_url = "{root_url}/ccadminx/custom/v1/testJobs"
extension_test_details_url = "{root_url}/ccadminx/custom/v1/{extensionName}/test/{date}"

# Server side extension linting endpoints
extension_lint_url = "{root_url}/ccadminx/custom/v1/lintJobs"

#  Blogs Endpoints
blogs_url = "{root_url}/ccadmin/v1/blogs"

#  Extensions Endpoints
extensions_url = "{root_url}/ccadmin/v1/extensions"
extensions_id_url = "{root_url}/ccadmin/v1/extensions/{id}"

#  Carriers Endpoints
carriers_url = "{root_url}/ccadmin/v1/carriers"
carriers_id_url = "{root_url}/ccadmin/v1/carriers/"

#  Asset Import/Export Endpoints
asset_upload_url = "{root_url}/ccadmin/v1/asset/upload"
asset_validate_url = "{root_url}/ccadmin/v1/asset/validate"
asset_validation_report_token_url = "{root_url}/ccadmin/v1/asset/validationReport/"
asset_import_url = "{root_url}/ccadmin/v1/asset/import"
asset_import_status_url = "{root_url}/ccadmin/v1/asset/importStatus"
asset_export_url = "{root_url}/ccadmin/v1/asset/export"

#  Skus Endpoints
skus_id_url = "{root_url}/ccadmin/v1/skus/{id}"
skus_url = "{root_url}/ccadmin/v1/skus"

#  Applications Endpoints
applications_id_url = "{root_url}/ccadmin/v1/applicationIds/{id}"
applications_ids_url = "{root_url}/ccadmin/v1/applicationIds"

#  Locales Endpoints
locales_url = "{root_url}/ccadmin/v1/locales"

#  Media Tag Endpoints
media_tags_url = "{root_url}/ccadmin/v1/mediaTags"

#  Orders Endpoints
orders_id_url = "{root_url}/ccadmin/v1/orders/{id}"
orders_url = "{root_url}/ccadmin/v1/orders"

#  Tax Processor Manager Endpoints
tax_processors_url = "{root_url}/ccadmin/v1/taxProcessors"
tax_processors_id_url = "{root_url}/ccadmin/v1/taxProcessors/{id}"

#  Country Region Endpoints
country_region_url = "{root_url}/ccadmin/v1/countries"
country_region_id_url = "{root_url}/ccadmin/v1/countries/{id}"

#  Report Filter Configuration Endpoints
report_filter_configuration_url = "{root_url}/ccadmin/v1/reportFilterConfigurations"
report_filter_configuration_id_url = "{root_url}/ccadmin/v1/reportFilterConfigurations/{id}"

#  Claimables Endpoints
claimables_url = "{root_url}/ccadmin/v1/claimables"
claimables_id_url = "{root_url}/ccadmin/v1/claimables/{id}"

#  Merchant Settings Endpoints
merchant_settings_profilePolicies_url = "{root_url}/ccadmin/v1/merchant/profilePolicies"
merchant_settings_timezone_url = "{root_url}/ccadmin/v1/merchant/timezone"
merchant_settings_profilePolicies_url = "{root_url}/ccadmin/v1/merchant/profilePolicies"
merchant_settings_paymentGateways_id_url = "{root_url}/ccadmin/v1/merchant/paymentGateways/{id}"
merchant_settings_paymentTypes_url = "{root_url}/ccadmin/v1/merchant/paymentTypes"
merchant_settings_paymentGateways_url = "{root_url}/ccadmin/v1/merchant/paymentGateways"
merchant_settings_cloudConfiguration_url = "{root_url}/ccadmin/v1/merchant/cloudConfiguration"
merchant_settings_priceListCurrency_url = "{root_url}/ccadmin/v1/merchant/priceListCurrency"
merchant_settings_timezone_url = "{root_url}/ccadmin/v1/merchant/timezone"
merchant_settings_billingCountries_url = "{root_url}/ccadmin/v1/merchant/billingCountries"
merchant_settings_paymentTypes_url = "{root_url}/ccadmin/v1/merchant/paymentTypes"
merchant_settings_billingCountries_url = "{root_url}/ccadmin/v1/merchant/billingCountries"
merchant_settings_priceLocale_url = "{root_url}/ccadmin/v1/merchant/priceLocale"
merchant_settings_merchant_url = "{root_url}/ccadmin/v1/merchant"
merchant_settings_id_url = "{root_url}/ccadmin/v1/merchant/{id}"
merchant_settings_merchant_url = "{root_url}/ccadmin/v1/merchant"
merchant_settings_contentLocales_url = "{root_url}/ccadmin/v1/merchant/contentLocales"
merchant_settings_remorsePeriod_url = "{root_url}/ccadmin/v1/merchant/remorsePeriod"
merchant_settings_itemPriceOverride_url = "{root_url}/ccadmin/v1/merchant/itemPriceOverride"
merchant_settings_robots_url = "{root_url}/ccadmin/v1/merchant/robots"

#  Publishing Endpoints
publishing_changes_url = "{root_url}/ccadmin/v1/publish/changes"
publishing_publish_url = "{root_url}/ccadmin/v1/publish"
publishing_schedules_id_url = "{root_url}/ccadmin/v1/publish/schedules/{id}"
publishing_schedules_url = "{root_url}/ccadmin/v1/publish/schedules"

#  Search Admin Endpoints
search_admin_schedule_url = "{root_url}/ccadmin/v1/search/schedule"
search_admin_index_url = "{root_url}/ccadmin/v1/search/index"

#  Failed WebHook Messages Endpoints
failed_webhook_messages_url = "{root_url}/ccadmin/v1/webhookFailedMessages"
failed_webhook_messages_id_url = "{root_url}/ccadmin/v1/webhookFailedMessages/{id}"

#  OAuth Endpoints
oauth_registry_url = "{root_url}/ccadmin/v1/registry"
oauth_logout_url = "{root_url}/ccadmin/v1/logout"
oauth_refresh_url = "{root_url}/ccadmin/v1/refresh"
oauth_login_url = "{root_url}/ccadmin/v1/login"
oauth_login_mfa_url = "{root_url}/ccadmin/v1/mfalogin"
oauth_id_url = "{root_url}/ccadmin/v1/api/{id}"
oauth_verify_url = "{root_url}/ccadmin/v1/verify"
oauth_api_url = "{root_url}/ccadmin/v1/api"

#  Files Endpoints
files_uploadTypes_url = "{root_url}/ccadmin/v1/files/uploadTypes"
files_mediaContents_url = "{root_url}/ccadmin/v1/files/mediaContents"
files_url = "{root_url}/ccadmin/v1/files"
files_id_url = "{root_url}/ccadmin/v1/files/{id}"
files_mediaUploadReport_url = "{root_url}/ccadmin/v1/files/mediaUploadReport/{token}"
files_deleteMediaItems_url = "{root_url}/ccadmin/v1/files/deleteMediaItems"

#  Products Endpoints
products_id_url = "{root_url}/ccadmin/v1/products/{id}"
products_url = "{root_url}/ccadmin/v1/products"

#  Variants Endpoints
variants_id_url = "{root_url}/ccadmin/v1/productVariants/{id}"
create_variants_url = "{root_url}/ccadmin/v1/productVariants"

#  Sites Endpoints
sites_id_url = "{root_url}/ccadmin/v1/sites/{id}"

#  Sites Settings Endpoints
sites_settings_id_url = "{root_url}/ccadmin/v1/sitesettings/{id}"
sites_settings_url = "{root_url}/ccadmin/v1/sitesettings"

#  Email Notifications Endpoints
email_notifications_url = "{root_url}/ccadmin/v1/emailNotifications"

#  Collections Endpoints
collections_url = "{root_url}/ccadmin/v1/collections"
collections_id_url = "{root_url}/ccadmin/v1/collections/"

#  WebHooks Endpoints
webhooks_id_url = "{root_url}/ccadmin/v1/webhooks/{id}"
webhooks_webhooks_url = "{root_url}/ccadmin/v1/webhooks"

#  Currency Endpoints
currency_currencies_url = "{root_url}/ccadmin/v1/currencies"
currency_id_url = "{root_url}/ccadmin/v1/currencies/{id}"

#  Announcement and Quick Links. Endpoints
announcement_posts_url = "{root_url}/ccadmin/v1/posts"

#  Reports Endpoints
reports_id_url = "{root_url}/ccadmin/v1/reports/{id}"
reports_export_url = "{root_url}/ccadmin/v1/reports/export"

#  Promotions Endpoints
promotions_url = "{root_url}/ccadmin/v1/promotions"
promotions_id_url = "{root_url}/ccadmin/v1/promotions/{id}"

#  Shipping Methods Endpoints
shipping_methods_url = "{root_url}/ccadmin/v1/shippingMethods"

#  Timezone Endpoints
timezone_timezones_url = "{root_url}/ccadmin/v1/timezones"
timezone_id_url = "{root_url}/ccadmin/v1/timezones/{id}"

#  Internal Profile Roles Endpoints
internal_profile_roles_adminRoles_url = "{root_url}/ccadmin/v1/adminRoles"

#  Health Check Endpoints
health_check_payments_url = "{root_url}/ccadmin/v1/healthCheck/payments"

#  Shipping Regions Endpoints
shipping_regions_url = "{root_url}/ccadmin/v1/shippingRegions"

#  Inventory Endpoints
inventory_inventories_url = "{root_url}/ccadmin/v1/inventories"
inventory_id_url = "{root_url}/ccadmin/v1/inventories/{id}"

#  Shopper Type Endpoints [Optionally takes the x-ccasset-language header to get translated content in another language.]
shopper_type_url = "{root_url}/ccadmin/v1/shopperTypes"
shopper_type_user_url = "{root_url}/ccadmin/v1/shopperTypes/user" #PUT requires the x-ccasset-language header so translated content can be set for a specific language.

#  Profiles Endpoints
profiles_url = "{root_url}/ccadmin/v1/profiles"
profiles_id_url = "{root_url}/ccadmin/v1/profiles/{id}"
profiles_reset_pwd_url = "{root_url}/ccadmin/v1/profiles/resetPassword"

# Product Type Endpoints
product_types_url = "{root_url}/ccadminui/v1/productTypes"
product_types_id_url = "{root_url}/ccadminui/v1/productTypes/{id}"

# Inventory Locations Endpoints
inventory_locations_url = "{root_url}/ccadmin/v1/locations"
inventory_locations_id_url = "{root_url}/ccadmin/v1/locations/{id}"
